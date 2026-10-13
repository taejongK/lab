"""LLM World 서버. 월드 상태의 유일한 원본.

uv run fastapi dev main.py   → http://127.0.0.1:8000
"""
import asyncio
import json
import logging
import re
import time
from collections import deque
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

import llm

log = logging.getLogger("uvicorn.error")

TICK = 0.2  # 초
IDLE_TICKS = 10  # 도착 후 다음 판단까지 대기
TILE = 16
MAP = [
    "####################",
    "#..................#",
    "#..####......####..#",
    "#..#..#......#..#..#",
    "#..#..#......#..#..#",
    "#..##.#......#.##..#",
    "#..................#",
    "#........###.......#",
    "#........#.#.......#",
    "#..................#",
    "#..................#",
    "#..####.......###..#",
    "#..#..........#....#",
    "#..................#",
    "####################",
]
LANDMARKS = {"home": (4, 4), "bakery": (15, 4), "well": (10, 8), "plaza": (10, 12)}
PERSONAS = {
    "mina": "You are Mina, a curious villager who likes to walk around and chat with people.",
    "tom": "You are Tom, the village baker. You care about your bakery but also need water from the well.",
}
NEARBY = 3  # 이 거리(맨해튼) 안의 엔티티를 '근처'로 본다
MEMORY = 5  # NPC가 기억하는 최근 사건 수
BUBBLE_TICKS = 20  # 말풍선 표시 시간
SAY_MAX = 80


def walkable(x: int, y: int) -> bool:
    return 0 <= y < len(MAP) and 0 <= x < len(MAP[0]) and MAP[y][x] != "#"


def bfs(start: tuple[int, int], goal: tuple[int, int]) -> list[tuple[int, int]]:
    """벽만 피하는 최단 경로 (start 제외). 엔티티 충돌은 이동 시점에 처리."""
    prev = {start: None}
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == goal:
            path = []
            while cur != start:
                path.append(cur)
                cur = prev[cur]
            return path[::-1]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nxt = (cur[0] + dx, cur[1] + dy)
            if nxt not in prev and walkable(*nxt):
                prev[nxt] = cur
                q.append(nxt)
    return []


def nearest_place(x: int, y: int) -> str:
    return min(LANDMARKS, key=lambda n: abs(LANDMARKS[n][0] - x) + abs(LANDMARKS[n][1] - y))


class World:
    def __init__(self) -> None:
        self.tick = 0
        self.entities = {
            "player": {"id": "player", "name": "Player", "kind": "player", "x": 9, "y": 10, "dir": "down"},
            "mina": {"id": "mina", "name": "Mina", "kind": "npc", "x": 4, "y": 4, "dir": "down"},
            "tom": {"id": "tom", "name": "Tom", "kind": "npc", "x": 15, "y": 4, "dir": "down"},
        }
        self.bubbles: dict[str, tuple[str, int]] = {}  # eid → (text, 사라질 틱)
        # NPC 전용 상태: 남은 경로, 막힌 틱 수, 다음 판단 가능 틱, 판단 중 여부
        self.npc = {eid: {"path": [], "blocked": 0, "ready_at": 0, "thinking": False, "events": deque(maxlen=MEMORY)}
                    for eid, e in self.entities.items() if e["kind"] == "npc"}

    def move(self, eid: str, dx: int, dy: int) -> bool:
        e = self.entities[eid]
        e["dir"] = {(1, 0): "right", (-1, 0): "left", (0, 1): "down", (0, -1): "up"}.get((dx, dy), e["dir"])
        nx, ny = e["x"] + dx, e["y"] + dy
        if walkable(nx, ny) and not any(o["x"] == nx and o["y"] == ny for o in self.entities.values()):
            e["x"], e["y"] = nx, ny
            return True
        return False

    def say(self, eid: str, text: str) -> None:
        """말풍선 + 근처 NPC 기억에 기록. 이게 '상호작용이 이동에 영향'을 주는 통로."""
        e = self.entities[eid]
        self.bubbles[eid] = (text, self.tick + BUBBLE_TICKS)
        for oid, s in self.npc.items():
            o = self.entities[oid]
            if oid != eid and abs(o["x"] - e["x"]) + abs(o["y"] - e["y"]) <= NEARBY:
                s["events"].append(f'{e["name"]} said: "{text}"')
                log.info("%s heard %s: %r", oid, eid, text)

    def go(self, eid: str, place: str) -> None:
        e = self.entities[eid]
        self.npc[eid]["path"] = bfs((e["x"], e["y"]), LANDMARKS[place])

    def idle_npcs(self) -> list[str]:
        return [eid for eid, s in self.npc.items()
                if not s["path"] and not s["thinking"] and self.tick >= s["ready_at"]]

    def step(self) -> None:
        self.tick += 1
        self.bubbles = {k: v for k, v in self.bubbles.items() if v[1] > self.tick}
        for eid, s in self.npc.items():
            if not s["path"]:
                continue
            e = self.entities[eid]
            nx, ny = s["path"][0]
            if self.move(eid, nx - e["x"], ny - e["y"]):
                s["path"].pop(0)
                s["blocked"] = 0
            else:
                s["blocked"] += 1
            # 목적지가 막혔거나(다른 엔티티가 서 있음) 오래 막히면 거기서 멈춘다
            if s["blocked"] > 5 or (len(s["path"]) == 1 and s["blocked"] > 0):
                s["path"] = []
            if not s["path"]:
                s["ready_at"] = self.tick + IDLE_TICKS
                place = nearest_place(e["x"], e["y"])
                s["events"].append(f"You arrived at {place}.")
                log.info("%s arrived near %s (%d,%d)", eid, place, e["x"], e["y"])

    def state(self) -> dict:
        return {
            "type": "state",
            "tick": self.tick,
            "entities": list(self.entities.values()),
            "bubbles": [{"id": k, "text": v[0]} for k, v in self.bubbles.items()],
        }


world = World()
clients: set[WebSocket] = set()


async def tick_loop() -> None:
    while True:
        await asyncio.sleep(TICK)
        world.step()
        msg = json.dumps(world.state())
        for ws in list(clients):
            try:
                await ws.send_text(msg)
            except Exception:
                clients.discard(ws)


def observe(eid: str, options: list[str]) -> str:
    e = world.entities[eid]
    near = [o["name"] for o in world.entities.values()
            if o["id"] != eid and abs(o["x"] - e["x"]) + abs(o["y"] - e["y"]) <= NEARBY]
    events = " ".join(world.npc[eid]["events"]) or "Nothing yet."
    # 현재 장소·wait는 선택지에서 뺀다: 0.8B는 관찰에 보인 현재 장소를 그대로 따라 말해 제자리에 고착됨 (devlog 2026-10-13)
    return (
        f"You are at: {nearest_place(e['x'], e['y'])}. Nearby: {', '.join(near) or 'nobody'}.\n"
        f"Recent events: {events}\n"
        f"Where do you go next? Pick one of: {', '.join(options)}.\n"
        'Format: {"target": <place>, "say": <one short sentence>}'
    )


async def decide(eid: str) -> str | None:
    """LLM에게 다음 목적지를 묻는다. 모델이 이름 댄 장소, 또는 None(무효 응답 → 대기 후 재시도).

    서버는 응답에서 선택지 이름을 찾아낼 뿐 대신 고르지 않는다 (랜덤 대체 금지).
    """
    e = world.entities[eid]
    here = nearest_place(e["x"], e["y"])
    options = [p for p in LANDMARKS if p != here]
    prompt = observe(eid, options)
    t = time.perf_counter()
    raw = await llm.ask(PERSONAS[eid] + " Reply with one JSON object only.", prompt)
    m = re.search("|".join(options), raw or "")  # 펜스·키 이름이 틀려도 장소 이름만 있으면 인정
    place = m.group(0) if m else None
    log.info("%s LLM %.2fs | at %s | -> %r => %s", eid, time.perf_counter() - t, here, raw, place or "INVALID")
    said = re.search(r'"say"\s*:\s*"([^"]{1,%d})"' % SAY_MAX, raw or "")
    if said:
        world.say(eid, said.group(1))
    return place


async def npc_loop() -> None:
    """할 일 없는 NPC를 하나씩 판단. 월드 틱과 분리되어 있어 판단이 느려도 월드는 멈추지 않는다."""
    while True:
        await asyncio.sleep(TICK)
        for eid in world.idle_npcs():
            world.npc[eid]["thinking"] = True
            try:
                place = await decide(eid)
                if place:
                    log.info("%s decided: move %s", eid, place)
                    world.go(eid, place)
            finally:
                world.npc[eid]["thinking"] = False
                world.npc[eid]["ready_at"] = world.tick + IDLE_TICKS  # 경로가 비면(이미 도착) 바로 재판단 방지


@asynccontextmanager
async def lifespan(app: FastAPI):
    await llm.load()
    tasks = [asyncio.create_task(tick_loop()), asyncio.create_task(npc_loop())]
    yield
    for t in tasks:
        t.cancel()


app = FastAPI(lifespan=lifespan)


@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    await ws.send_json({
        "type": "init",
        "you": "player",
        "map": MAP,
        "tile": TILE,
        "landmarks": [{"name": n, "x": x, "y": y} for n, (x, y) in LANDMARKS.items()],
    })
    clients.add(ws)
    try:
        while True:
            msg = await ws.receive_json()
            # 신뢰 경계: 클라이언트 입력은 한 칸 이동만 허용
            if msg.get("type") == "move" and (msg.get("dx"), msg.get("dy")) in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                world.move("player", msg["dx"], msg["dy"])
            elif msg.get("type") == "say" and isinstance(msg.get("text"), str) and msg["text"].strip():
                world.say("player", msg["text"].strip()[:SAY_MAX])
    except WebSocketDisconnect:
        clients.discard(ws)


app.mount("/", StaticFiles(directory=Path(__file__).parent.parent / "frontend", html=True), name="frontend")

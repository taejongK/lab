"""LLM World 서버. 월드 상태의 유일한 원본.

uv run fastapi dev main.py   → http://127.0.0.1:8000
"""
import asyncio
import json
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

TICK = 0.2  # 초
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


def walkable(x: int, y: int) -> bool:
    return 0 <= y < len(MAP) and 0 <= x < len(MAP[0]) and MAP[y][x] != "#"


class World:
    def __init__(self) -> None:
        self.tick = 0
        self.entities = {
            "player": {"id": "player", "name": "Player", "kind": "player", "x": 9, "y": 10, "dir": "down"},
            "mina": {"id": "mina", "name": "Mina", "kind": "npc", "x": 4, "y": 4, "dir": "down"},
            "tom": {"id": "tom", "name": "Tom", "kind": "npc", "x": 15, "y": 4, "dir": "down"},
        }
        self.bubbles: dict[str, str] = {}

    def move(self, eid: str, dx: int, dy: int) -> None:
        e = self.entities[eid]
        e["dir"] = {(1, 0): "right", (-1, 0): "left", (0, 1): "down", (0, -1): "up"}.get((dx, dy), e["dir"])
        nx, ny = e["x"] + dx, e["y"] + dy
        if walkable(nx, ny) and not any(o["x"] == nx and o["y"] == ny for o in self.entities.values()):
            e["x"], e["y"] = nx, ny

    def step(self) -> None:
        self.tick += 1

    def state(self) -> dict:
        return {
            "type": "state",
            "tick": self.tick,
            "entities": list(self.entities.values()),
            "bubbles": [{"id": k, "text": v} for k, v in self.bubbles.items()],
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(tick_loop())
    yield
    task.cancel()


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
    except WebSocketDisconnect:
        clients.discard(ws)


app.mount("/", StaticFiles(directory=Path(__file__).parent.parent / "frontend", html=True), name="frontend")

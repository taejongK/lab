"""세계 상태와 규칙. AI를 모른다. AI의 제안은 apply()를 통과해야만 세계를 바꾼다."""
import json
from collections import deque

DIRS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
CHANGE_TYPES = ("set_fact", "set_object_state", "kill", "jail", "move", "give")


def load_scenario(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class World:
    def __init__(self, s):
        self.s = s
        self.map = s["map"]
        self.rooms = s["rooms"]
        self.tick = 0
        self.player_id = s["player"]["id"]
        self.chars = {}
        for c in [s["player"]] + s["characters"]:
            self.chars[c["id"]] = {
                "id": c["id"], "name": c["name"], "x": c["x"], "y": c["y"], "sheet": c.get("sheet", {}),
                "routine": c.get("routine", []), "alive": True, "jailed": False, "path": [], "pending": None,
                "hold_until": 0,
                "memory": {"known": [], "feelings": []},
            }
            for text in c.get("knows", []):
                self.remember(c["id"], "initial", text)
        self.objects = {o["id"]: {**o, "state": None, "holder": None} for o in s["objects"]}
        self.roles = {k: {**v} for k, v in s["roles"].items()}
        self.facts, self.events = [], []
        self.announced = []  # engine가 비워 가며 NPC 반응을 일으킨다
        self.debug_notice = None  # None | "all" | "none"
        names = {r["name"] for r in self.rooms}
        for c in self.chars.values():
            bad = set(c["routine"]) - names
            assert not bad, f"{c['id']}의 일과에 없는 방: {bad}"

    # --- 공간
    def walkable(self, x, y):
        return 0 <= y < len(self.map) and 0 <= x < len(self.map[y]) and self.map[y][x] in ".+"

    def room_of(self, x, y):
        for r in self.rooms:
            if r["x0"] <= x <= r["x1"] and r["y0"] <= y <= r["y1"]:
                return r["name"]
        return None

    def room_center(self, name):
        r = next((r for r in self.rooms if r["name"] == name), None)
        return None if r is None else ((r["x0"] + r["x1"]) // 2, (r["y0"] + r["y1"]) // 2)

    def room_spot(self, name, cid):
        """캐릭터마다 방 안의 다른 자리. 한 칸에 겹쳐 서지 않도록."""
        r = next(r for r in self.rooms if r["name"] == name)
        i = list(self.chars).index(cid)
        if r.get("spots"):  # 창살 앞처럼 서야 할 자리를 시나리오가 정한 경우
            return tuple(r["spots"][i % len(r["spots"])])
        return r["x0"] + i * 2 % (r["x1"] - r["x0"] + 1), r["y0"] + i % (r["y1"] - r["y0"] + 1)

    def path(self, start, goal):
        """start에서 goal까지 칸 목록(start 제외). 없으면 None."""
        prev, q = {start: None}, deque([start])
        while q:
            p = q.popleft()
            if p == goal:
                out = []
                while p != start:
                    out.append(p)
                    p = prev[p]
                return out[::-1]
            for dx, dy in DIRS.values():
                n = (p[0] + dx, p[1] + dy)
                if n not in prev and self.walkable(*n):
                    prev[n] = p
                    q.append(n)
        return None

    def pos(self, eid):
        e = self.chars.get(eid) or self.objects.get(eid)
        if e is None:
            return None
        holder = e.get("holder")
        return self.pos(holder) if holder else (e["x"], e["y"])

    def near(self, a, b):
        """인터랙션 가능 거리. 창살(B) 한 칸 너머도 닿는다 — 갇혀도 대화할 수 있도록."""
        pa, pb = self.pos(a), self.pos(b)
        if pa is None or pb is None:
            return False
        d = abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
        if d <= 1:
            return True
        if d == 2 and (pa[0] == pb[0] or pa[1] == pb[1]):
            return self.map[(pa[1] + pb[1]) // 2][(pa[0] + pb[0]) // 2] == "B"
        return False

    def same_room(self, eid):
        """eid와 같은 방에 있는 산 캐릭터. 문턱에 있으면 아무도 없다."""
        x, y = self.pos(eid)
        room = self.room_of(x, y)
        if room is None:
            return []
        return [c["id"] for c in self.chars.values()
                if c["id"] != eid and c["alive"] and self.room_of(c["x"], c["y"]) == room]

    def move_player(self, direction):
        p = self.chars[self.player_id]
        if direction not in DIRS or not p["alive"]:
            return False
        nx, ny = p["x"] + DIRS[direction][0], p["y"] + DIRS[direction][1]
        if not self.walkable(nx, ny):
            return False
        p["x"], p["y"] = nx, ny
        return True

    def rooms_at(self, x, y):
        """그 칸이 속한 방. 문턱은 맞닿은 방 모두에 속한다."""
        room = self.room_of(x, y)
        if room:
            return {room}
        return {r for r in (self.room_of(x + dx, y + dy) for dx, dy in DIRS.values()) if r}

    def witnesses(self, actor, target=None):
        """이 행위를 알아챌 수 있는 산 캐릭터. 행위자 쪽과 대상 쪽 방을 모두 본다."""
        rooms = self.rooms_at(*self.pos(actor)) if actor else set()
        if target and self.pos(target):
            rooms |= self.rooms_at(*self.pos(target))
        out = [c["id"] for c in self.chars.values() if c["id"] != actor and c["alive"]
               and (self.room_of(c["x"], c["y"]) in rooms or c["id"] == target)]
        return out

    # --- 메모리
    def remember(self, cid, kind, text, source=None):
        """kind: initial | witnessed | heard | announced"""
        self.chars[cid]["memory"]["known"].append(
            {"tick": self.tick, "kind": kind, "text": text, "source": source})

    def feel(self, cid, text):
        self.chars[cid]["memory"]["feelings"].append({"tick": self.tick, "text": text})

    def announce(self, text):
        """모두가 아는 공표. 원인처럼 공개되지 않은 내용은 넣지 않는다."""
        self.facts.append({"tick": self.tick, "text": text, "public": True})
        self.announced.append(text)
        for c in self.chars.values():
            if c["alive"]:
                self.remember(c["id"], "announced", text)

    # --- 변경
    def role_of(self, cid):
        return [r for r, v in self.roles.items() if v["holder"] == cid]

    def apply(self, ch):
        """AI가 제안한 변경 하나를 검증해 적용한다. (성공 여부, 사유)"""
        t, cid, oid = ch.get("type"), ch.get("character"), ch.get("object")
        c, o = self.chars.get(cid), self.objects.get(oid)
        if t == "set_fact":
            if not ch.get("text"):
                return False, "내용 없음"
            # AI는 공표할 수 없다. 공표는 코드만 한다 — 아는 사람의 범위가 AI 판단으로 넓어지지 않도록
            self.facts.append({"tick": self.tick, "text": ch["text"], "public": False})
            return True, ""
        if t == "set_object_state":
            if o is None:
                return False, f"없는 오브젝트 {oid}"
            o["state"] = ch.get("text")
            return True, ""
        if t == "give":
            if o is None:
                return False, f"없는 오브젝트 {oid}"
            if cid is None:  # 내려놓기: 들고 있던 사람의 자리에 남는다
                o["x"], o["y"] = self.pos(oid)
                o["holder"] = None
                return True, ""
            if c is None or not c["alive"]:
                return False, f"받을 수 없는 캐릭터 {cid}"
            o["holder"] = cid
            return True, ""
        if c is None:
            return False, f"없는 캐릭터 {cid}"
        if not c["alive"]:
            return False, f"이미 죽은 캐릭터 {cid}"
        if t == "kill":
            if cid == self.player_id:
                return False, "플레이어는 죽지 않는다"
            self._kill(c)
            return True, ""
        if t == "jail":
            if cid != self.player_id:
                return False, "플레이어만 가둘 수 있다"
            cell = self.s.get("jail_cell")
            if cell is None or c["jailed"]:
                return False, "가둘 수 없다"
            c["x"], c["y"], c["jailed"] = cell[0], cell[1], True
            return True, ""
        if t == "move":
            if cid == self.player_id:
                return False, "플레이어는 AI가 옮기지 않는다"
            goal = self.room_center(ch.get("text") or "")
            route = goal and self.path((c["x"], c["y"]), goal)
            if route is None or not goal:
                return False, f"갈 수 없는 곳 {ch.get('text')}"
            c["path"] = route
            c["hold_until"] = self.tick + len(route) + self.s.get("routine_period", 40)
            return True, ""
        return False, f"알 수 없는 변경 {t}"

    def _kill(self, c):
        c["alive"], c["path"], c["pending"] = False, [], None
        for o in self.objects.values():
            if o["holder"] == c["id"]:
                o["x"], o["y"], o["holder"] = c["x"], c["y"], None
        for role, v in self.roles.items():
            if v["holder"] != c["id"]:
                continue
            nxt = next((i for i in v["succession"] if i in self.chars and self.chars[i]["alive"]), None)
            v["holder"] = nxt
            heir = f"새 {role}: {self.chars[nxt]['name']}" if nxt else f"뒤를 이을 {role} 없음"
            self.announce(f"{c['name']}이(가) 세상을 떠났다. {heir}")

    # --- AI에게 줄 정보
    def public_char(self, cid):
        c = self.chars[cid]
        return {"id": cid, "name": c["name"], "alive": c["alive"], "room": self.room_of(c["x"], c["y"]),
                "roles": self.role_of(cid)}

    def public_object(self, oid):
        o = self.objects[oid]  # state는 뺀다. 독이 들었는지는 보아서 알 수 없다
        return {"id": oid, "name": o["name"], "description": o["description"], "held_by": o["holder"]}

    def surroundings(self, cid):
        x, y = self.pos(cid)
        room = self.room_of(x, y)
        return {
            "room": room,
            "people_here": [self.public_char(i) for i in self.same_room(cid)],
            "bodies_here": [c["name"] for c in self.chars.values()
                            if not c["alive"] and room and self.room_of(c["x"], c["y"]) == room],
            # 다른 사람이 지닌 물건은 보이지 않는다
            "objects_here": [self.public_object(i) for i, o in self.objects.items()
                             if room and o["holder"] in (None, cid) and self.room_of(*self.pos(i)) == room],
            "holding": [self.public_object(i) for i, o in self.objects.items() if o["holder"] == cid],
        }

    def full_view(self):
        """게임 마스터용. 모든 것이 보인다."""
        return {
            "story": self.s["story"],
            "strictness": self.s.get("strictness", "open"),
            "tick": self.tick,
            "characters": [{**self.public_char(i), "sheet": c["sheet"], "jailed": c["jailed"],
                            "knows": c["memory"]["known"]}
                           for i, c in self.chars.items()],
            "objects": [{**self.public_object(i), "state": o["state"], "room": self.room_of(*self.pos(i))}
                        for i, o in self.objects.items()],
            "rooms": [r["name"] for r in self.rooms],
            "roles": self.roles,
            "facts": self.facts,
            "recent_events": self.events[-30:],
        }

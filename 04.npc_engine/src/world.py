"""세계 상태와 규칙. AI를 모른다. AI의 제안은 apply()를 통과해야만 세계를 바꾼다."""
import json
import pathlib
from collections import deque

DIRS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
CHANGE_TYPES = ("set_fact", "set_object_state", "kill", "jail", "move", "give")


def load_scenario(path):
    with open(path, encoding="utf-8") as f:
        s = json.load(f)
    if s.get("sprites_file"):
        with open(pathlib.Path(path).parent / s["sprites_file"], encoding="utf-8") as f:
            s["sprites"] = json.load(f)
    return s


def check_sprites(sprites, size=16):
    """도트 데이터 형식 검사. 나중에 창작자 에디터도 이 형식으로 저장한다."""
    for group, items in sprites.items():
        for name, sp in items.items():
            for frame, rows in sp["frames"].items():
                where = f"{group}/{name}/{frame}"
                assert len(rows) == size and all(len(r) == size for r in rows), f"{where}: {size}x{size}가 아니다"
                unknown = set("".join(rows)) - set(sp["palette"]) - {"."}
                assert not unknown, f"{where}: 팔레트에 없는 색 {unknown}"


def check_scenario(s):
    """플레이 전 검사. 문제를 창작자가 읽을 문장으로 돌려준다. 저장 중인 초안이 들어오므로 어떤 값에도 터지지 않는다."""
    try:
        return _problems(s)
    except (KeyError, TypeError, ValueError, AttributeError, IndexError, AssertionError) as e:
        return [f"[전체] 시나리오 형식이 잘못됐습니다: {e!r}"]


def _problems(s):
    p = []
    if not s.get("title", "").strip():
        p.append("[세계관] 게임 제목이 없습니다")
    if not s.get("story", "").strip():
        p.append("[세계관] 배경 이야기가 없습니다")
    if s.get("strictness") not in ("open", "strict"):
        p.append("[세계관] 줄거리 방식은 open 또는 strict여야 합니다")
    elif s["strictness"] == "strict" and not s.get("goal", "").strip():
        p.append("[세계관] 엄격한 진행에는 반드시 지킬 목표가 필요합니다")

    grid, rooms = s["map"], s["rooms"]
    if not grid or len({len(r) for r in grid}) != 1 or set("".join(grid)) - set(".#+B"):
        return p + ["[공간] 지도는 같은 길이의 줄로, 바닥·벽·문·창살만으로 이뤄져야 합니다"]
    h, w = len(grid), len(grid[0])
    walk = lambda x, y: 0 <= y < h and 0 <= x < w and grid[y][x] in ".+"
    names = [r["name"] for r in rooms]
    if not rooms:
        p.append("[공간] 방이 하나도 없습니다")
    if len(set(names)) != len(names) or not all(n.strip() for n in names):
        p.append("[공간] 방 이름은 비어 있지 않고 서로 달라야 합니다")
    covered = {}
    for r in rooms:
        if not (0 <= r["x0"] <= r["x1"] < w and 0 <= r["y0"] <= r["y1"] < h):
            p.append(f"[공간] 방 '{r['name']}'이(가) 지도 밖으로 나갑니다")
        for y in range(r["y0"], r["y1"] + 1):
            for x in range(r["x0"], r["x1"] + 1):
                if (x, y) in covered:
                    p.append(f"[공간] 방 '{r['name']}'과(와) '{covered[x, y]}'이(가) 겹칩니다")
                    break
                covered[x, y] = r["name"]
            else:
                continue
            break
    loose = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == "." and (x, y) not in covered]
    if loose:
        p.append(f"[공간] 어느 방에도 속하지 않은 바닥 {len(loose)}칸이 있습니다 (예: {loose[0]})")
    if s.get("jail_cell") and not walk(*s["jail_cell"]):
        p.append("[공간] 감옥 칸은 바닥이어야 합니다")

    chars = [s["player"]] + s["characters"]
    ids = [c["id"] for c in chars] + [o["id"] for o in s["objects"]]
    if len(set(ids)) != len(ids):
        p.append("[캐릭터] 캐릭터와 물건의 id가 겹칩니다")
    for c in chars:
        if not c.get("name", "").strip():
            p.append(f"[캐릭터] {c['id']}의 이름이 없습니다")
        if not walk(c["x"], c["y"]):
            p.append(f"[공간] {c.get('name')}의 시작 위치가 바닥이 아닙니다")
        bad = set(c.get("routine", [])) - set(names)
        if bad:
            p.append(f"[캐릭터] {c.get('name')}의 일과에 없는 방이 있습니다: {sorted(bad)}")
    for o in s["objects"]:
        if not o.get("name", "").strip() or not o.get("description", "").strip():
            p.append(f"[공간] 물건 {o['id']}의 이름과 설명이 필요합니다")
        if not walk(o["x"], o["y"]):
            p.append(f"[공간] {o.get('name')}의 위치가 바닥이 아닙니다")

    sprites = s.get("sprites", {})
    try:
        check_sprites(sprites)
    except (AssertionError, KeyError, TypeError, AttributeError) as e:
        p.append(f"[도트] {e}")
    for c in chars:
        if not {"down", "up", "side"} <= set(sprites.get("characters", {}).get(c["id"], {}).get("frames", {})):
            p.append(f"[도트] {c.get('name')}에게 정면·뒷면·옆면 그림이 모두 필요합니다")
    for o in s["objects"]:
        if "idle" not in sprites.get("objects", {}).get(o["id"], {}).get("frames", {}):
            p.append(f"[도트] {o.get('name')}의 그림이 없습니다")
    for ch in set("".join(grid)):
        if "idle" not in sprites.get("tiles", {}).get(ch, {}).get("frames", {}):
            p.append(f"[도트] 타일 '{ch}'의 그림이 없습니다")

    char_ids = {c["id"] for c in chars}
    for role, v in s["roles"].items():
        if not role.strip() or v["holder"] not in char_ids or set(v["succession"]) - char_ids:
            p.append(f"[규칙] 역할 '{role}'의 이름이나 맡은 캐릭터가 잘못됐습니다")
    for a in s["base_actions"]:
        if not a["label"].strip() or a["targets"] not in ("character", "object", "any") or set(a.get("actors", [])) - char_ids:
            p.append(f"[규칙] 행위 '{a['label']}'의 설정이 잘못됐습니다")
    for e in s.get("schedule", []):
        if not e["description"].strip() or not isinstance(e["at"], int) or e["at"] < 0 or (e.get("actor") and e["actor"] not in char_ids):
            p.append(f"[규칙] 사건 '{e['description']}'의 설정이 잘못됐습니다")
    if p:
        return p

    # 일과대로 걸어갈 수 있어야 한다. 못 가면 NPC가 아무 말 없이 멈춘다
    world = World(s)
    for c in s["characters"]:
        for room in c.get("routine", []):
            if world.path((c["x"], c["y"]), world.room_spot(room, c["id"])) is None:
                p.append(f"[공간] {c['name']}이(가) 일과의 '{room}'까지 걸어갈 수 없습니다")
    return p


class World:
    def __init__(self, s):
        self.s = s
        check_sprites(s.get("sprites", {}))
        self.map = s["map"]
        self.rooms = s["rooms"]
        self.tick = 0
        self.player_id = s["player"]["id"]
        self.chars = {}
        for c in [s["player"]] + s["characters"]:
            self.chars[c["id"]] = {
                "id": c["id"], "name": c["name"], "x": c["x"], "y": c["y"], "sheet": c.get("sheet", {}),
                "routine": c.get("routine", []), "alive": True, "jailed": False, "path": [], "pending": None,
                "hold_until": 0, "engaged_until": 0,
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
            "fixed_goal": self.s.get("goal"),
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

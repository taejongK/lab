"""게임 흐름: 행위 → 게임 마스터 판정 → 코드 검증 → 메모리 → NPC 반응."""
import threading
from collections import deque

from world import CHANGE_TYPES, World

MAX_DEPTH = 2  # 반응이 반응을 낳는 사슬의 길이. 호출이 무한정 늘지 않도록 끊는다
MAX_SUGGESTED = 3
MAX_REPLY_TRIES = 3
MAX_SCHEDULE_RETRIES = 3
SILENT_LINE = "……"


class AIError(Exception):
    """API 오류, 거절, 잘못된 응답, 호출 상한 초과. 게임은 멈추지 않고 상태도 바꾸지 않는다."""


class Engine:
    def __init__(self, scenario, ai, max_calls=400):
        self.w = World(scenario)
        self.ai = ai
        self.max_calls = max_calls
        self.calls = 0
        self.lock = threading.RLock()
        self.queue = deque()
        self.busy = False
        self.offered = {}  # 대상별로 플레이어에게 보여 준 행위. 브라우저 입력 검증용
        self.stats = {"changes_rejected": [], "check_failed": 0, "reply_fallback": 0, "ai_errors": []}
        self.fired = set()

    def _ask(self, kind, payload):
        try:
            with self.lock:
                if self.calls >= self.max_calls:
                    raise AIError(f"호출 상한 {self.max_calls} 도달")
                self.calls += 1
            return self.ai.ask(kind, payload)
        except AIError as e:
            with self.lock:
                self.stats["ai_errors"].append(f"{kind}: {e}")
            print(f"[AI 오류] {kind}: {e}", flush=True)
            raise

    # --- 시간
    def step(self):
        """1틱: 일정, NPC 이동, 대기 중인 행위."""
        with self.lock:
            w = self.w
            w.tick += 1
            for sch in w.s.get("schedule", []):
                if w.tick >= sch["at"]:
                    self.fire_schedule(sch["id"])
            for c in w.chars.values():
                if c["id"] != w.player_id and c["alive"]:
                    self._step_npc(c)

    def fire_schedule(self, sid):
        with self.lock:
            if sid in self.fired:
                return False
            sch = next((s for s in self.w.s.get("schedule", []) if s["id"] == sid), None)
            if sch is None:
                return False
            self.fired.add(sid)
            self.queue.append({"type": "event", "actor": sch.get("actor"), "label": sch["description"],
                               "target": None, "depth": 0, "scheduled": True,
                               "witnesses": self.w.witnesses(sch.get("actor"))})
            return True

    def _step_npc(self, c):
        w = self.w
        pending = c["pending"]
        if pending:
            if w.near(c["id"], pending["target"]):
                c["pending"], c["path"] = None, []
                self.queue.append({"type": "event", "actor": c["id"], "label": pending["label"],
                                   "target": pending["target"], "depth": pending["depth"],
                                   "witnesses": w.witnesses(c["id"], pending["target"])})
                return
            # 코드가 경로를 찾는다. AI는 어디로 갈지만 정한다
            route = w.path((c["x"], c["y"]), w.pos(pending["target"]))
            if route is None:
                c["pending"] = None
                return
            c["path"] = route
        if c["path"]:
            c["x"], c["y"] = c["path"].pop(0)
            return
        period = w.s.get("routine_period", 40)
        if c["routine"] and w.tick >= c["hold_until"]:  # AI가 보낸 곳에서는 일과가 잠시 멈춘다
            room = c["routine"][(w.tick // period) % len(c["routine"])]
            if w.room_of(c["x"], c["y"]) != room:
                c["path"] = w.path((c["x"], c["y"]), w.room_spot(room, c["id"])) or []

    # --- 사건 큐
    def pump(self):
        """대기열에서 하나를 처리한다. 처리할 게 있었으면 True."""
        with self.lock:
            if not self.queue:
                self.busy = False
                return False
            job = self.queue.popleft()
            self.busy = True
        try:
            if job["type"] == "event":
                self._resolve(job)
            else:
                self._decide(job)
        except AIError:
            with self.lock:
                actor = job.get("actor")
                if job.get("scheduled"):  # 일정이 API 오류로 사라지면 이야기가 멈춘다. 몇 번 다시 시도한다
                    job["retries"] = job.get("retries", 0) + 1
                    if job["retries"] <= MAX_SCHEDULE_RETRIES:
                        self.queue.append(job)
                elif job["type"] == "event" and actor == self.w.player_id:
                    self.w.remember(actor, "witnessed", f"'{job['label']}'을(를) 시도했지만 아무 일도 일어나지 않았다.")
        finally:
            with self.lock:
                self.busy = False
        return True

    def drain(self):
        while self.pump():
            pass

    def _resolve(self, job):
        w = self.w
        with self.lock:
            actor, target = job["actor"], job.get("target")
            if actor and (actor not in w.chars or not w.chars[actor]["alive"]):
                return
            candidates = [c for c in job.get("witnesses", []) if w.chars[c]["alive"]]  # 행위 시점에 계산한 후보
            payload = {
                "world": w.full_view(),
                "action": {"actor": actor, "label": job["label"], "target": target,
                           "scheduled_event": bool(job.get("scheduled"))},
                "witness_candidates": candidates,
            }
        r = self._ask("resolve", payload)
        with self.lock:
            for ch in r.get("changes", []):
                ok, why = w.apply(ch) if ch.get("type") in CHANGE_TYPES else (False, "허용되지 않은 변경")
                if not ok:
                    self.stats["changes_rejected"].append({"change": ch, "why": why})
            label = job["label"]
            noticed = self._noticed(r.get("noticed", []), candidates, actor, label)
            w.events.append({"tick": w.tick, "actor": actor, "label": label, "target": target,
                             "outcome": r.get("outcome", ""), "noticed_by": [c for c, _ in noticed]})
            if actor and r.get("outcome"):
                w.remember(actor, "witnessed", f"내가 '{label}'을(를) 했다. 결과: {r['outcome']}")
            for cid, text in noticed:
                if w.chars[cid]["alive"]:
                    w.remember(cid, "witnessed", text)
            reactors = [cid for cid, _ in noticed]
            reason = {cid: text for cid, text in noticed}
            for text in w.announced:
                for c in w.chars.values():
                    if c["alive"] and c["id"] != w.player_id and c["id"] not in reason:
                        reason[c["id"]] = text
                        reactors.append(c["id"])
            w.announced.clear()
            if job["depth"] < MAX_DEPTH:
                for cid in reactors:
                    if cid != w.player_id and w.chars[cid]["alive"]:
                        self.queue.append({"type": "decide", "actor": cid, "trigger": reason[cid],
                                           "depth": job["depth"] + 1})

    def _noticed(self, proposed, candidates, actor, label):
        """코드가 계산한 후보 안에서만 인정한다. 후보 밖은 지목해도 기록하지 않는다."""
        mode = self.w.debug_notice
        name = self.w.chars[actor]["name"] if actor else "누군가"
        if mode == "all":
            return [(c, f"{name}이(가) '{label}'을(를) 하는 것을 보았다.") for c in candidates]
        if mode == "none":
            return []
        out = []
        for n in proposed:
            if n.get("character") in candidates and n.get("perceived"):
                out.append((n["character"], n["perceived"]))
        return out

    def _allowed_actions(self, cid):
        return [a for a in self.w.s["base_actions"] if cid in a.get("actors", [cid])]

    def _npc_actions(self, cid):
        """대화는 말하기(speech)로 하므로 NPC의 행위 목록에서 뺀다."""
        return [a for a in self._allowed_actions(cid) if a["id"] != "talk"]

    def _character_view(self, cid):
        """캐릭터가 아는 것만 담는다. 세계 전체는 넣지 않는다."""
        w = self.w
        c = w.chars[cid]
        # shortcut: 메모리를 통째로 넣는다. 수백 건을 넘겨 비용이 문제 되면 관련성 검색으로 바꾼다
        return {"me": {"id": cid, "name": c["name"], "sheet": c["sheet"], "roles": w.role_of(cid)},
                "memory": c["memory"], "now": w.surroundings(cid), "tick": w.tick}

    def _decide(self, job):
        w = self.w
        with self.lock:
            cid = job["actor"]
            if not w.chars[cid]["alive"]:
                return
            payload = {
                **self._character_view(cid),
                "what_just_happened": job["trigger"],
                "rooms": [r["name"] for r in w.rooms],
                "possible_actions": [a["label"] for a in self._npc_actions(cid)],
            }
        r = self._ask("decide", payload)
        speech = r.get("speech")
        if speech:  # 듣는 사람에게 닿기 전에 확인한다. 어긋나면 그 말은 하지 않은 것으로 친다
            check = self._ask("check", {"knowledge": payload["memory"], "me": payload["me"], "now": payload["now"],
                                        "heard_just_now": job["trigger"], "reply": speech})
            if not check.get("ok"):
                speech = None
                with self.lock:
                    self.stats["check_failed"] += 1
        with self.lock:
            if not w.chars[cid]["alive"]:
                return
            c = w.chars[cid]
            if r.get("feeling"):
                w.feel(cid, r["feeling"])
            if speech:
                w.remember(cid, "witnessed", f"내가 말함: \"{speech}\"")
                self._overheard(cid, None, speech)
            action = next((a for a in self._npc_actions(cid) if a["label"] == r.get("action")), None)
            target = r.get("target")
            people = set(w.same_room(cid))
            items = {i for i, o in w.objects.items()
                     if o["holder"] in (None, cid) and w.room_of(*w.pos(i)) == w.room_of(c["x"], c["y"])}
            kinds = {"character": people, "object": items, "any": people | items}
            if action and target in kinds[action["targets"]]:
                label = action["label"]
                c["pending"] = {"label": label, "target": target, "depth": job["depth"]}
            elif r.get("go_room"):
                ok, why = w.apply({"type": "move", "character": cid, "text": r["go_room"]})
                if not ok:
                    self.stats["changes_rejected"].append({"change": r["go_room"], "why": why})

    def _overheard(self, speaker, addressee, text):
        """같은 방에 있으면 듣는다. 누가 한 말인지 함께 저장하고, 사실로 취급하지 않는다."""
        w = self.w
        name = w.chars[speaker]["name"]
        to = f" {w.chars[addressee]['name']}에게" if addressee else ""
        for cid in w.same_room(speaker):
            if cid != addressee:
                w.remember(cid, "heard", f"{name}이(가){to} 말함: \"{text}\"", source=speaker)

    # --- 플레이어
    def interact(self, target):
        """대상 앞의 행위 목록: 창작자의 기본 행위 + AI가 상황을 보고 더한 행위."""
        w = self.w
        with self.lock:
            pid = w.player_id
            if not self._target_ok(target):
                return None
            is_char = target in w.chars
            alive = w.chars[target]["alive"] if is_char else True
            base = []
            for a in self._allowed_actions(pid):
                kind = "character" if is_char else "object"
                if a["targets"] not in (kind, "any"):
                    continue
                if not alive and not a.get("on_dead"):
                    continue
                base.append({"id": a["id"], "label": a["label"], "ai": False})
            payload = {
                **self._character_view(pid),
                "target": w.public_char(target) if is_char else w.public_object(target),
                "world_truth_for_gm": w.full_view(),
                "base_actions": [a["label"] for a in base],
            }
        extras = []
        if alive:
            try:
                r = self._ask("suggest", payload)
                seen = {a["label"] for a in base}
                for label in r.get("actions", []):
                    label = (label or "").strip()
                    if label and len(label) <= 40 and label not in seen and len(extras) < MAX_SUGGESTED:
                        seen.add(label)
                        extras.append({"id": None, "label": label, "ai": True})
            except AIError:
                pass  # 기본 행위만으로도 플레이는 이어진다
        actions = base + extras
        with self.lock:
            self.offered[target] = {a["label"]: a for a in actions}
        return actions

    def _target_ok(self, target):
        w = self.w
        return (target in w.chars or target in w.objects) and target != w.player_id and w.near(w.player_id, target)

    def act(self, target, label):
        """제안한 행위만 받는다. 브라우저 입력은 믿지 않는다."""
        with self.lock:
            offered = self.offered.get(target, {})
            if label not in offered or not self._target_ok(target) or offered[label].get("id") == "talk":
                return False
            self.offered.pop(target)
            self.queue.append({"type": "event", "actor": self.w.player_id, "label": label,
                               "target": target, "depth": 0,
                               "witnesses": self.w.witnesses(self.w.player_id, target)})
            return True

    def say(self, target, text):
        """플레이어의 말에 NPC가 답한다. 답은 그 캐릭터가 아는 것과 어긋나면 다시 만든다."""
        w = self.w
        text = (text or "").strip()[:500]
        with self.lock:
            if not text or target not in w.chars or not w.chars[target]["alive"] or not self._target_ok(target):
                return None
            pid = w.player_id
            pname = w.chars[pid]["name"]
            w.remember(target, "heard", f"{pname}이(가) 나에게 말함: \"{text}\"", source=pid)
            self._overheard(pid, target, text)
            view = self._character_view(target)
        retry_note = None
        speech, suggested, feeling = None, [], None
        for _ in range(MAX_REPLY_TRIES):
            try:
                r = self._ask("reply", {**view, "player_said": text, "previous_attempt_problem": retry_note})
                check = self._ask("check", {"knowledge": view["memory"], "me": view["me"], "now": view["now"],
                                            "heard_just_now": text, "reply": r.get("speech", "")})
            except AIError:
                break
            if check.get("ok"):
                speech, suggested, feeling = r.get("speech"), r.get("suggested_replies", []), r.get("feeling")
                break
            with self.lock:
                self.stats["check_failed"] += 1
            retry_note = check.get("reason") or "일관성 문제"
        with self.lock:
            if not w.chars[target]["alive"]:  # 답을 기다리는 사이에 죽었다
                return None
            if not speech:
                self.stats["reply_fallback"] += 1
                speech = SILENT_LINE
            name = w.chars[target]["name"]
            if feeling:
                w.feel(target, feeling)
            w.remember(target, "witnessed", f"내가 {pname}에게 말함: \"{speech}\"")
            w.remember(pid, "heard", f"{name}: \"{speech}\"", source=target)
            self._overheard(target, pid, speech)
        return {"speech": speech, "suggested_replies": suggested[:3]}

    # --- 화면
    def view(self):
        """플레이어에게 보이는 것: 같은 방의 사람과 물건, 자기 메모리."""
        w = self.w
        with self.lock:
            p = w.chars[w.player_id]
            room = w.room_of(p["x"], p["y"])
            def visible(x, y, eid):  # 같은 방 + 창살 너머처럼 손이 닿는 곳
                return (room is not None and w.room_of(x, y) == room) or w.near(w.player_id, eid)
            return {
                "map": w.map, "tick": w.tick, "room": room, "busy": self.busy or bool(self.queue),
                "player": {"x": p["x"], "y": p["y"], "name": p["name"], "jailed": p["jailed"]},
                "people": [{"id": c["id"], "name": c["name"], "x": c["x"], "y": c["y"], "alive": c["alive"]}
                           for c in w.chars.values() if c["id"] != w.player_id and visible(c["x"], c["y"], c["id"])],
                "objects": [{"id": i, "name": o["name"], "x": o["x"], "y": o["y"]}
                            for i, o in w.objects.items() if not o["holder"] and visible(o["x"], o["y"], i)],
                "holding": [o["name"] for o in w.objects.values() if o["holder"] == w.player_id],
                "known": p["memory"]["known"][-40:],
                "ai_errors": len(self.stats["ai_errors"]),
                "schedule": [s["id"] for s in w.s.get("schedule", [])],
            }

    def metrics(self):
        return {"calls": self.calls, **self.stats, **getattr(self.ai, "usage", {})}

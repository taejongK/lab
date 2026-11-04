"""API 없이 엔진 흐름을 확인하기 위한 가짜 응답. 판단의 질은 전혀 검증하지 못한다."""


class FakeAI:
    usage = {"model": "fake"}

    def __init__(self):
        self.fail_checks = 0  # 다음 N번의 일관성 확인을 실패시킨다
        self.script = {}  # kind -> 다음 응답을 강제한다 (잘못된 AI 응답 시험용)

    def ask(self, kind, p):
        if kind in self.script:
            return self.script.pop(kind)
        return getattr(self, kind)(p)

    def suggest(self, p):
        holding = p["now"]["holding"]
        return {"actions": [f"{p['target']['name']}에 {h['name']} 쓰기" for h in holding]}

    def resolve(self, p):
        a, w = p["action"], p["world"]
        names = {c["id"]: c["name"] for c in w["characters"]}
        changes, outcome = [], f"{a['label']}: 시도했다."
        if a["label"] == "집어 들기":
            changes.append(_ch("give", character=a["actor"], object=a["target"]))
        elif a["label"] == "체포하기":
            changes.append(_ch("jail", character=a["target"]))
        elif a.get("target") and "쓰기" in a["label"]:
            changes.append(_ch("set_object_state", object=a["target"], text="독이 들었다"))
            outcome = "아무도 모르게 끝냈다."
        elif a["scheduled_event"]:
            for o in w["objects"]:
                if o["state"]:
                    changes.append(_ch("kill", character=a["actor"]))
                    outcome = "술을 마시고 쓰러졌다."
        noticed = [{"character": c, "perceived": f"{names.get(a['actor'], '누군가')}의 일을 보았다."}
                   for c in p["witness_candidates"]]
        return {"outcome": outcome, "noticed": noticed, "changes": changes}

    def decide(self, p):
        guard = "체포하기" in p["possible_actions"]
        suspect = next((c for c in p["now"]["people_here"] if c["id"] == "player"), None)
        saw_player = any("약초상" in m["text"] for m in p["memory"]["known"] if m["kind"] == "witnessed")
        if guard and suspect and saw_player:
            return {"speech": "멈춰라!", "feeling": "수상하다", "action": "체포하기", "target": "player", "go_room": None}
        return {"speech": None, "feeling": "불안하다", "action": None, "target": None, "go_room": None}

    def reply(self, p):
        known = p["memory"]["known"]
        latest = next((m["text"] for m in reversed(known) if m["kind"] != "heard"), "아는 게 없다")
        return {"speech": f"내가 아는 건 이것뿐이다: {latest}", "feeling": None, "suggested_replies": ["더 말해 줘"]}

    def check(self, p):
        if self.fail_checks > 0:
            self.fail_checks -= 1
            return {"ok": False, "reason": "가짜 실패"}
        return {"ok": True, "reason": ""}


def _ch(t, character=None, object=None, text=None):
    return {"type": t, "character": character, "object": object, "text": text}

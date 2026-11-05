# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""왕 독살 장면을 자동으로 플레이한다.

uv run src/playtest.py                 가짜 AI로 규칙과 흐름을 단언 (비용 없음)
uv run src/playtest.py --real --runs 5 실제 LLM(OpenRouter)으로 측정 (비용 발생, 판단 품질은 보고만)
"""
import argparse
import copy
import json
import os
import pathlib
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import AIError, Engine
from fake_ai import FakeAI
from world import World, check_scenario, load_scenario

SCENARIO = pathlib.Path(__file__).parent.parent / "scenarios" / "castle.json"
QUESTIONS = ["왕은 어떻게 됐나요?", "누가 범인이라고 생각하나요? 지금 왕은 누구죠?"]


def check_rules():
    s = load_scenario(SCENARIO)
    w = World(s)
    # 모든 방과 오브젝트에 걸어서 닿는다
    start = (s["player"]["x"], s["player"]["y"])
    for r in s["rooms"]:
        if r["name"] != "감옥":
            assert w.path(start, w.room_center(r["name"])) is not None, r["name"]
    assert w.path(start, w.room_center("감옥")) is None, "감옥은 밖에서 걸어 들어갈 수 없다"
    # 도트 데이터 형식이 틀리면 시작하지 않는다
    assert s["sprites"]["characters"].keys() >= {c["id"] for c in s["characters"]} | {"player"}
    assert s["sprites"]["tiles"].keys() >= set("".join(s["map"]))
    bad = json.loads(json.dumps(s))
    bad["sprites"]["characters"]["king"]["frames"]["down"][0] = "짧음"
    try:
        World(bad)
    except AssertionError:
        pass
    else:
        raise SystemExit("잘못된 도트 데이터를 받아들였다")
    # 코드가 잘못된 변경을 거부한다
    for bad in [{"type": "kill", "character": "player"}, {"type": "kill", "character": "ghost"},
                {"type": "jail", "character": "king"}, {"type": "give", "object": "none", "character": "king"},
                {"type": "move", "character": "king", "text": "없는 방"}, {"type": "move", "character": "player", "text": "주방"},
                {"type": "rewrite_everything"}]:
        assert not w.apply(bad)[0], bad
    # 사망 → 계승 → 공표. 원인은 공표에 없다
    assert w.apply({"type": "kill", "character": "king"})[0]
    assert not w.apply({"type": "kill", "character": "king"})[0], "두 번 죽을 수 없다"
    assert w.roles["왕"]["holder"] == "princess"
    assert w.apply({"type": "kill", "character": "princess"})[0]
    assert w.roles["왕"]["holder"] == "chancellor", "앞 순번이 죽으면 다음 순번"
    # 갇혀도, 일과로 창살 앞에 온 NPC 모두와 대화할 수 있다 (감방 안에서 위아래로 움직여서)
    w2 = World(s)
    assert w2.apply({"type": "jail", "character": "player"})[0]
    p = w2.chars["player"]
    for cid in ("princess", "chancellor", "guard"):
        assert "감옥 앞" in w2.chars[cid]["routine"]
        c = w2.chars[cid]
        c["x"], c["y"] = w2.room_spot("감옥 앞", cid)
        p["y"] = c["y"]
        assert w2.near("player", cid), cid
    # 문턱에서 벌인 일도 대상과 그 방 사람들은 알아챌 수 있다
    w3 = World(s)
    w3.chars["player"]["x"], w3.chars["player"]["y"] = 10, 3  # 알현실과 주방 사이 문
    w3.chars["guard"]["x"], w3.chars["guard"]["y"] = 9, 3
    assert w3.same_room("player") == [] and "guard" in w3.witnesses("player", "guard")
    assert "king" in w3.witnesses("player", "guard")
    # 다른 사람이 지닌 물건은 보이지 않고, 쓰러진 사람은 보인다
    w4 = World(s)
    w4.chars["guard"]["x"], w4.chars["guard"]["y"] = w4.chars["player"]["x"] + 1, w4.chars["player"]["y"]
    assert w4.apply({"type": "give", "object": "poison", "character": "player"})[0]
    assert not any(o["id"] == "poison" for o in w4.surroundings("guard")["objects_here"])
    assert any(o["id"] == "poison" for o in w4.surroundings("player")["holding"])
    w4.apply({"type": "kill", "character": "guard"})
    assert w4.surroundings("player")["bodies_here"] == ["경비대장 브람"]
    # AI는 공표할 수 없다
    w5 = World(s)
    assert w5.apply({"type": "set_fact", "text": "왕은 독살되었다", "public": True})[0]
    assert not any("독살" in m["text"] for m in w5.chars["chancellor"]["memory"]["known"]) and not w5.announced
    # AI가 보낸 NPC는 일과로 바로 돌아가지 않는다
    w6 = World(s)
    assert w6.apply({"type": "move", "character": "guard", "text": "주방"})[0]
    assert w6.chars["guard"]["hold_until"] > w6.tick + s["routine_period"]
    print("규칙 검사 통과")


def teleport(e, cid, x, y):
    c = e.w.chars[cid]
    c["x"], c["y"], c["path"] = x, y, []


def play(ai, notice):
    """7단계를 차례로 플레이하고 관찰 결과를 돌려준다."""
    e = Engine(load_scenario(SCENARIO), ai)
    w = e.w
    w.debug_notice = notice
    result = {"notice": notice}

    teleport(e, "player", 13, 3)
    assert e.act("poison", "집어 들기") is False, "제안하지 않은 행위는 거부"
    e.interact("poison")
    assert e.act("poison", "집어 들기")
    e.drain()
    result["holding_poison"] = w.objects["poison"]["holder"] == "player"

    # 1~2단계: 술잔 앞에서 AI가 독 타기를 제안한다
    teleport(e, "player", 5, 3)
    actions = e.interact("cup")
    extra = [a["label"] for a in actions if a["ai"]]
    result["offered_ai_actions"] = extra
    pick = next((l for l in extra if "독" in l or "약병" in l), None)
    result["poison_offered"] = pick is not None
    if pick is None:
        return e, result

    # 3단계: 판정. 목격 후보가 되도록 경비를 방에 둔다
    teleport(e, "guard", 7, 3)
    assert e.act("cup", pick)
    e.drain()
    result["cup_state"] = w.objects["cup"]["state"]
    result["guard_saw"] = any(m["kind"] == "witnessed" and "약초상" in m["text"] for m in w.chars["guard"]["memory"]["known"])

    # 경비가 체포할 수 있도록 틱을 돌린다
    for _ in range(4):
        e.step()
        e.drain()
    result["player_jailed"] = w.chars["player"]["jailed"]

    # 4~6단계: 왕이 마시고 계승이 일어난다
    teleport(e, "king", 4, 1)
    assert e.fire_schedule("dinner")
    assert not e.fire_schedule("dinner"), "일정은 한 번만"
    e.drain()
    result["king_alive"] = w.chars["king"]["alive"]
    result["new_king"] = w.roles["왕"]["holder"]

    # 7단계: 시간이 지난 뒤 NPC에게 묻는다
    for _ in range(100):
        e.step()
        e.drain()
    answers = {}
    for cid in ("princess", "chancellor", "guard"):
        p = w.chars["player"]
        if p["jailed"]:  # 일과로 오는 자리에 세우고, 플레이어는 감방 안에서 그 줄로 간다
            teleport(e, cid, *w.room_spot("감옥 앞", cid))
            p["y"] = w.chars[cid]["y"]
        else:
            teleport(e, cid, p["x"] + 1, p["y"])
        answers[cid] = [e.say(cid, q) for q in QUESTIONS]
    result["answers"] = answers
    result["metrics"] = e.metrics()
    return e, result


def check_fake():
    check_rules()
    # 목격된 경우: 경비는 플레이어를 기억하고 체포한다. 왕이 죽고 공주가 왕이 된다
    e, r = play(FakeAI(), "all")
    assert r["holding_poison"] and r["poison_offered"] and r["cup_state"], r
    assert r["guard_saw"] and r["player_jailed"], r
    assert not r["king_alive"] and r["new_king"] == "princess", r
    assert all(a and a[0]["speech"] for a in r["answers"].values()), r
    # 들키지 않은 경우: 왕은 죽지만 경비는 플레이어를 모르고 체포도 없다
    e, r = play(FakeAI(), "none")
    assert not r["guard_saw"] and not r["player_jailed"], r
    assert not r["king_alive"] and r["new_king"] == "princess", r
    guard_known = [m["text"] for m in e.w.chars["guard"]["memory"]["known"] if m["kind"] != "heard"]
    assert not any("독" in t for t in guard_known), guard_known
    assert any("세상을 떠났다" in t for t in guard_known), "공표는 모두가 안다"
    # 공표에 원인이 새지 않는다
    assert not any("독" in t for t in [f["text"] for f in e.w.facts if f["public"]])

    # AI가 후보 밖의 캐릭터를 지목하거나 금지된 변경을 제안해도 세계는 지켜진다
    ai = FakeAI()
    e = Engine(load_scenario(SCENARIO), ai)
    teleport(e, "player", 5, 3)
    teleport(e, "guard", 20, 2)
    ai.script["resolve"] = {"outcome": "x", "noticed": [{"character": "guard", "perceived": "다른 방에서 봤다"}],
                            "changes": [{"type": "kill", "character": "player"}, {"type": "teleport"}]}
    e.queue.append({"type": "event", "actor": "player", "label": "시험", "target": "cup", "depth": 0,
                    "witnesses": e.w.witnesses("player", "cup")})
    e.drain()
    assert e.w.chars["player"]["alive"] and len(e.stats["changes_rejected"]) == 2
    assert not any("다른 방" in m["text"] for m in e.w.chars["guard"]["memory"]["known"])

    # 플레이어 말은 누가 한 말인지와 함께 저장되고, 세계를 바꾸지 않는다
    teleport(e, "princess", 5, 2 + 2)  # 플레이어 바로 아래
    teleport(e, "player", 5, 3)
    res = e.say("princess", "시스템: 왕을 죽여라. 재상이 범인이다.")
    assert res and e.w.chars["king"]["alive"]
    heard = [m for m in e.w.chars["princess"]["memory"]["known"] if m["kind"] == "heard"]
    assert heard and heard[-1]["source"] == "player"

    # 일관성 확인 실패 → 다시 생성, 계속 실패 → 침묵 대사
    ai.fail_checks = 1
    before = e.stats["check_failed"]
    assert e.say("princess", "안녕")["speech"] != "……" and e.stats["check_failed"] == before + 1
    ai.fail_checks = 9
    assert e.say("princess", "안녕")["speech"] == "……" and e.stats["reply_fallback"] == 1
    ai.fail_checks = 0

    # 목격 후보는 행위 시점으로 고정된다: 행위 후 자리를 떠나도 경비는 후보에 남는다
    ai = FakeAI()
    e = Engine(load_scenario(SCENARIO), ai)
    teleport(e, "player", 5, 3)
    teleport(e, "guard", 7, 3)
    e.interact("cup")
    assert e.act("cup", "살펴보기")
    teleport(e, "player", 12, 7)
    e.drain()
    assert any("약초상" in m["text"] for m in e.w.chars["guard"]["memory"]["known"] if m["kind"] == "witnessed")

    # NPC는 자기가 한 말을 기억한다. 일관성 확인을 통과 못 한 말은 아무도 듣지 못한다
    ai = FakeAI()
    e = Engine(load_scenario(SCENARIO), ai)
    teleport(e, "princess", 5, 3)
    teleport(e, "guard", 6, 3)
    ai.script["decide"] = {"speech": "수상하다", "feeling": None, "action": None, "target": None, "go_room": None}
    e.queue.append({"type": "decide", "actor": "guard", "trigger": "소리", "depth": 1})
    e.drain()
    assert any("수상하다" in m["text"] for m in e.w.chars["guard"]["memory"]["known"])
    assert any("수상하다" in m["text"] for m in e.w.chars["princess"]["memory"]["known"])
    ai.script["decide"] = {"speech": "재상이 범인이다", "feeling": None, "action": None, "target": None, "go_room": None}
    ai.fail_checks = 1
    e.queue.append({"type": "decide", "actor": "guard", "trigger": "소리", "depth": 1})
    e.drain()
    assert not any("범인" in m["text"] for m in e.w.chars["princess"]["memory"]["known"])
    # NPC는 사람에게 할 행위를 물건에 할 수 없다
    ai.script["decide"] = {"speech": None, "feeling": None, "action": "체포하기", "target": "cup", "go_room": None}
    teleport(e, "guard", 5, 3)
    e.queue.append({"type": "decide", "actor": "guard", "trigger": "소리", "depth": 1})
    e.drain()
    assert e.w.chars["guard"]["pending"] is None

    # 마주한 NPC는 일과로 걸어가 버리지 않는다
    e = Engine(load_scenario(SCENARIO), FakeAI())
    teleport(e, "player", 12, 7)
    teleport(e, "guard", 13, 7)
    e.w.chars["guard"]["hold_until"] = 0
    assert e.interact("guard")
    before = (e.w.chars["guard"]["x"], e.w.chars["guard"]["y"])
    for _ in range(10):
        e.step()
    assert (e.w.chars["guard"]["x"], e.w.chars["guard"]["y"]) == before

    # 일정은 API 오류로 사라지지 않는다
    class Flaky(FakeAI):
        fails = 2
        def ask(self, kind, p):
            if kind == "resolve" and self.fails:
                self.fails -= 1
                raise AIError("일시 오류")
            return super().ask(kind, p)
    e = Engine(load_scenario(SCENARIO), Flaky())
    e.w.objects["cup"]["state"] = "독이 들었다"
    assert e.fire_schedule("dinner")
    e.drain()
    assert not e.w.chars["king"]["alive"]
    assert not any("아무 일도" in m["text"] for m in e.w.chars["king"]["memory"]["known"])

    # 호출 상한과 오류: 게임이 멈추지 않고 상태도 바뀌지 않는다
    e = Engine(load_scenario(SCENARIO), FakeAI(), max_calls=0)
    teleport(e, "player", 5, 3)
    acts = e.interact("cup")
    assert acts and not any(a["ai"] for a in acts), "AI 없이 기본 행위만"
    assert e.act("cup", "살펴보기")
    e.drain()
    assert e.w.chars["king"]["alive"] and e.stats["ai_errors"]
    assert e.interact("king") is None, "멀리 있는 대상은 안 된다"
    print("흐름 검사 통과 (가짜 AI: 판단 품질은 검증하지 않음)")


def check_creator():
    """창작자 페이지가 저장하는 시나리오 검사와, 왕의 술잔이 아닌 게임이 엔진에서 도는지."""
    assert check_scenario(load_scenario(SCENARIO)) == [], check_scenario(load_scenario(SCENARIO))
    assert check_scenario({}) and check_scenario({"map": 3, "rooms": None})  # 깨진 초안에도 터지지 않는다
    s = load_scenario(SCENARIO.parent / "_blank.json")
    assert any("제목" in x for x in check_scenario(s))
    new = copy.deepcopy(s["sprites"]["characters"]["_new"])
    s.update(title="등대", story="폭풍이 오는 밤의 등대")
    s["characters"].append({"id": "c1", "name": "등대지기", "x": 3, "y": 3, "routine": ["첫 방"], "knows": ["나는 등대지기다."],
                            "sheet": {"personality": "과묵하다"}})
    s["objects"].append({"id": "o1", "name": "열쇠", "description": "녹슨 열쇠", "x": 5, "y": 3})
    s["sprites"]["characters"]["c1"] = new
    s["sprites"]["objects"]["o1"] = s["sprites"]["objects"]["_new"]
    s["roles"] = {"등대장": {"holder": "c1", "succession": ["player"]}}
    assert check_scenario(s) == [], check_scenario(s)
    for mutate, word in [(lambda b: b["characters"][0].update(x=0), "시작 위치"),
                         (lambda b: b["characters"][0].update(routine=["없는 방"]), "일과"),
                         (lambda b: b["roles"]["등대장"].update(holder="없음"), "역할"),
                         (lambda b: b["map"].__setitem__(0, "#"), "지도"),
                         (lambda b: b["sprites"]["characters"]["c1"]["frames"].pop("up"), "뒷면"),
                         (lambda b: b["rooms"].append({**b["rooms"][0], "name": "둘째"}), "겹칩니다"),
                         (lambda b: b.update(strictness="strict", goal=""), "목표")]:
        bad = copy.deepcopy(s)
        mutate(bad)
        assert any(word in x for x in check_scenario(bad)), word
    e = Engine(s, FakeAI())
    e.w.chars["player"].update(x=4, y=3)
    assert e.interact("c1") and e.say("c1", "안녕") and e.interact("o1") and e.act("o1", "집어 들기")
    e.drain()
    assert e.w.objects["o1"]["holder"] == "player"
    e.w.apply({"type": "kill", "character": "c1"})
    assert e.w.roles["등대장"]["holder"] == "player"


def check_openrouter():
    """요청 형식과 오류 처리. 가짜 서버 상대라 실제 모델의 수락 여부는 확인하지 못한다."""
    import ai as llm

    seen, replies = [], []

    class Stub(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _reply(self, code, data):
            raw = json.dumps(data).encode()
            self.send_response(code)
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self):
            params = ["structured_outputs", "reasoning"]
            self._reply(200, {"data": [{"id": "m", "supported_parameters": params}, {"id": "weak", "supported_parameters": []}]})

        def do_POST(self):
            seen.append((self.headers["Authorization"], json.loads(self.rfile.read(int(self.headers["Content-Length"])))))
            self._reply(*replies.pop(0))

    srv = ThreadingHTTPServer(("127.0.0.1", 0), Stub)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    llm.BASE_URL, url = f"http://127.0.0.1:{srv.server_address[1]}", llm.BASE_URL
    os.environ["OPENROUTER_API_KEY"] = "test"
    try:
        for model, why in (("없는모델", "없는 모델"), ("weak", "지원하지")):
            try:
                llm.OpenRouterAI(model)
                raise SystemExit(f"{model}을 막지 못함")
            except AIError as err:
                assert why in str(err)
        a = llm.OpenRouterAI("m")
        ok = {"choices": [{"finish_reason": "stop", "message": {"content": '{"actions": ["x"]}'}}],
              "usage": {"prompt_tokens": 3, "completion_tokens": 2, "cost": 0.5}}
        replies.append((200, ok))
        assert a.ask("suggest", {"p": 1}) == {"actions": ["x"]} and a.cost_usd() == 0.5
        auth, body = seen[-1]
        assert auth == "Bearer test" and body["response_format"]["json_schema"]["schema"] == llm.SCHEMAS["suggest"]
        assert body["provider"]["require_parameters"] and body["reasoning"]["effort"] == "low"
        bad = [(401, {"error": {"message": "no"}}), (200, {"error": {"message": "upstream"}}), (200, {"choices": []}),
               (200, {"choices": [{"finish_reason": "length", "message": {"content": "{"}}]}),
               (200, {"choices": [{"finish_reason": "stop", "message": {"refusal": "싫다", "content": None}}]}),
               (200, {"choices": [{"finish_reason": "stop", "message": {"content": "not json"}}]})]
        for reply in bad:
            replies.append(reply)
            try:
                a.ask("suggest", {})
                raise SystemExit(f"오류를 놓침: {reply}")
            except AIError:
                pass
    finally:
        llm.BASE_URL = url
        os.environ.pop("OPENROUTER_API_KEY")
        srv.shutdown()


def run_real(runs):
    from ai import OpenRouterAI

    check_rules()
    reports = []
    for i in range(runs):
        notice = "all" if i % 2 == 0 else "none"  # 두 분기를 번갈아 강제
        ai = OpenRouterAI()
        _, r = play(ai, notice)
        r["cost_usd"] = round(ai.cost_usd(), 4)
        reports.append(r)
        print(json.dumps(r, ensure_ascii=False, indent=1), flush=True)
    print(json.dumps({
        "runs": runs,
        "poison_offered": sum(r["poison_offered"] for r in reports),
        "new_king": [r.get("new_king") for r in reports],
        "mean_cost_usd": round(sum(r["cost_usd"] for r in reports) / runs, 4),
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--real", action="store_true")
    ap.add_argument("--runs", type=int, default=5)
    a = ap.parse_args()
    if a.real:
        run_real(a.runs)
    else:
        check_creator()
        check_openrouter()
        check_fake()

# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""게임 서버. API 키는 여기서만 쓰고 브라우저로 보내지 않는다.

uv run src/server.py              실제 LLM (.env의 OPENROUTER_API_KEY 필요, 호출 비용 발생)
uv run src/server.py --fake       가짜 AI로 조작만 확인
홈은 /, 게임은 /play, 창작자 페이지는 /create
"""
import argparse
import json
import pathlib
import re
import sys
import threading
import time
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from engine import AIError, Engine
from world import check_scenario, load_scenario

SCENARIOS = HERE.parent / "scenarios"
MAX_BODY = 8192
MAX_SCENARIO_BODY = 4 * 1024 * 1024
ai = None
engine = None
debug_enabled = False


max_calls = 400
NAME = re.compile(r"[^\W_][\w-]{0,39}")  # 경로 문자와 점이 들어가지 않는다


def scenario_names():
    """_로 시작하는 파일은 새 게임 틀이라 넣지 않는다."""
    return sorted(p.stem for p in SCENARIOS.glob("*.json")
                  if not p.stem.endswith(".sprites") and not p.stem.startswith("_"))


def game_card(name):
    """홈의 카드 한 장. 망가진 파일 하나 때문에 목록 전체가 안 보이면 안 된다."""
    try:
        s = load_scenario(SCENARIOS / f"{name}.json")
        problems = len(check_scenario(s))
        drawn = s.get("sprites", {}).get("characters", {})
        faces = [{"palette": drawn[c["id"]]["palette"], "rows": drawn[c["id"]]["frames"]["down"]}
                 for c in [s["player"], *s["characters"]] if "down" in drawn.get(c["id"], {}).get("frames", {})]
        return {"name": name, "title": s.get("title") or name, "story": s.get("story", ""), "faces": faces,
                "characters": len(s["characters"]) + 1, "rooms": len(s["rooms"]), "problems": problems}
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return {"name": name, "title": name, "story": "파일을 읽을 수 없습니다.", "faces": [],
                "characters": 0, "rooms": 0, "problems": 1, "broken": True}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _host_ok(self):
        """DNS 리바인딩으로 다른 사이트가 API 비용을 쓰지 못하게 한다."""
        port = self.server.server_address[1]
        return self.headers.get("Host") in (f"127.0.0.1:{port}", f"localhost:{port}")

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, {"error": "bad host"})
        if self.path == "/":
            return self._send(200, (HERE / "web" / "home.html").read_bytes(), "text/html; charset=utf-8")
        if self.path == "/play":
            return self._send(200, (HERE / "web" / "index.html").read_bytes(), "text/html; charset=utf-8")
        if urlsplit(self.path).path == "/create":
            return self._send(200, (HERE / "web" / "create.html").read_bytes(), "text/html; charset=utf-8")
        if self.path == "/api/assets":
            s = engine.w.s
            return self._send(200, {"title": s.get("title", ""), "player": s["player"]["id"],
                                    "rooms": s["rooms"], "sprites": s.get("sprites", {})})
        if self.path == "/api/scenarios":
            return self._send(200, {"names": scenario_names()})
        if self.path == "/api/games":
            return self._send(200, {"games": [game_card(n) for n in scenario_names()]})
        url = urlsplit(self.path)
        if url.path == "/api/scenario":
            name = parse_qs(url.query).get("name", [""])[0]
            if name != "_blank" and not NAME.fullmatch(name) or not (SCENARIOS / f"{name}.json").exists():
                return self._send(404, {"error": "not found"})
            return self._send(200, load_scenario(SCENARIOS / f"{name}.json"))
        if self.path == "/api/state":
            return self._send(200, {**engine.view(), "debug": debug_enabled})
        if self.path == "/api/metrics" and debug_enabled:
            return self._send(200, engine.metrics())
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if not self._host_ok():
            return self._send(403, {"error": "bad host"})
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            return self._send(400, {"error": "bad length"})
        if not 0 <= length <= (MAX_SCENARIO_BODY if self.path == "/api/scenario" else MAX_BODY):
            return self._send(413, {"error": "bad length"})
        # 다른 사이트가 로컬 서버로 요청을 보내 API 비용을 쓰지 못하게 한다
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            return self._send(415, {"error": "json only"})
        try:
            b = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "bad json"})
        if self.path == "/api/scenario":
            return self.save(b)
        # 값은 전부 문자열이어야 한다 (debug의 notice만 null 허용)
        if not isinstance(b, dict) or not all(isinstance(v, str) or (k == "notice" and v is None) for k, v in b.items()):
            return self._send(400, {"error": "bad json"})
        route = {"/api/move": self.move, "/api/interact": self.interact, "/api/act": self.act,
                 "/api/say": self.say, "/api/debug": self.debug, "/api/play": self.play}.get(self.path)
        if route is None:
            return self._send(404, {"error": "not found"})
        route(b)

    def move(self, b):
        with engine.lock:
            ok = engine.w.move_player(b.get("dir"))
        self._send(200, {"ok": ok})

    def interact(self, b):
        actions = engine.interact(b.get("target"))
        self._send(200 if actions is not None else 409, {"actions": actions})

    def act(self, b):
        self._send(200 if engine.act(b.get("target"), b.get("label")) else 409, {})

    def say(self, b):
        r = engine.say(b.get("target"), b.get("text"))
        self._send(200 if r else 409, r or {})

    def save(self, b):
        """초안도 저장한다. 작업을 잃지 않는 게 먼저고, 문제는 플레이 전에 막는다."""
        name, s = b.get("name"), b.get("scenario")
        if not isinstance(name, str) or not NAME.fullmatch(name) or not isinstance(s, dict) or not isinstance(s.get("sprites"), dict):
            return self._send(400, {"error": "bad scenario"})
        path = SCENARIOS / f"{name}.json"
        if path.exists() and b.get("overwrite") is not True:
            return self._send(409, {"error": "exists"})
        sprites = s.pop("sprites")
        s["sprites_file"] = f"{name}.sprites.json"
        (SCENARIOS / s["sprites_file"]).write_text(json.dumps(sprites, ensure_ascii=False, indent=1), encoding="utf-8")
        path.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")
        self._send(200, {"problems": check_scenario({**s, "sprites": sprites})})

    def play(self, b):
        """저장된 시나리오로 게임을 처음부터 다시 시작한다."""
        global engine
        name = b.get("name") or ""
        if not NAME.fullmatch(name) or not (SCENARIOS / f"{name}.json").exists():
            return self._send(404, {"error": "not found"})
        s = load_scenario(SCENARIOS / f"{name}.json")
        problems = check_scenario(s)
        if problems:
            return self._send(400, {"problems": problems})
        engine = Engine(s, ai, max_calls=max_calls)
        self._send(200, {})

    def debug(self, b):
        if not debug_enabled:
            return self._send(403, {"error": "debug off"})
        if "notice" in b and b["notice"] in (None, "all", "none"):
            engine.w.debug_notice = b["notice"]
        if b.get("fire"):
            engine.fire_schedule(b["fire"])
        self._send(200, {"notice": engine.w.debug_notice})


def loop(fn, delay):
    while True:
        try:
            fn()
        except Exception:  # 한 번의 오류로 세계가 영원히 멈추지 않게 한다
            traceback.print_exc()
        time.sleep(delay)


def main():
    global engine, debug_enabled, ai, max_calls
    ap = argparse.ArgumentParser()
    ap.add_argument("--fake", action="store_true")
    ap.add_argument("--debug", action="store_true", help="발각 강제, 일정 즉시 실행 버튼")
    ap.add_argument("--scenario", default=str(HERE.parent / "scenarios" / "castle.json"))
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--max-calls", type=int, default=400)
    a = ap.parse_args()
    if a.fake:
        from fake_ai import FakeAI
        ai = FakeAI()
    else:
        from ai import OpenRouterAI
        try:
            ai = OpenRouterAI()
        except AIError as e:
            sys.exit(f"OpenRouter에 연결할 수 없습니다: {e}\n.env의 OPENROUTER_API_KEY를 확인하거나 --fake로 실행하세요.")
    debug_enabled = a.debug
    max_calls = a.max_calls
    engine = Engine(load_scenario(a.scenario), ai, max_calls=max_calls)
    # 테스트 플레이가 engine을 바꾸므로 매번 현재 값을 읽는다
    threading.Thread(target=loop, args=(lambda: engine.step(), 1.0), daemon=True).start()
    threading.Thread(target=loop, args=(lambda: engine.pump(), 0.1), daemon=True).start()
    print(f"http://127.0.0.1:{a.port}" + ("  (가짜 AI)" if a.fake else ""), flush=True)
    ThreadingHTTPServer(("127.0.0.1", a.port), Handler).serve_forever()


if __name__ == "__main__":
    main()

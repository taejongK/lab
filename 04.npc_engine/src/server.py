# /// script
# requires-python = ">=3.10"
# dependencies = ["anthropic"]
# ///
"""게임 서버. API 키는 여기서만 쓰고 브라우저로 보내지 않는다.

uv run src/server.py              실제 Claude (ANTHROPIC_API_KEY 필요, 호출 비용 발생)
uv run src/server.py --fake       가짜 AI로 조작만 확인
"""
import argparse
import json
import pathlib
import sys
import threading
import time
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from engine import Engine
from world import load_scenario

MAX_BODY = 8192
engine = None
debug_enabled = False


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
            return self._send(200, (HERE / "web" / "index.html").read_bytes(), "text/html; charset=utf-8")
        if self.path == "/api/assets":
            s = engine.w.s
            return self._send(200, {"rooms": s["rooms"], "sprites": s.get("sprites", {})})
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
        if not 0 <= length <= MAX_BODY:
            return self._send(413, {"error": "bad length"})
        # 다른 사이트가 로컬 서버로 요청을 보내 API 비용을 쓰지 못하게 한다
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            return self._send(415, {"error": "json only"})
        try:
            b = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "bad json"})
        # 값은 전부 문자열이어야 한다 (debug의 notice만 null 허용)
        if not isinstance(b, dict) or not all(isinstance(v, str) or (k == "notice" and v is None) for k, v in b.items()):
            return self._send(400, {"error": "bad json"})
        route = {"/api/move": self.move, "/api/interact": self.interact, "/api/act": self.act,
                 "/api/say": self.say, "/api/debug": self.debug}.get(self.path)
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
    global engine, debug_enabled
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
        import anthropic
        from ai import ClaudeAI
        try:
            ai = ClaudeAI()
            ai.client.models.retrieve(ai.model)
        except (anthropic.AnthropicError, TypeError) as e:
            sys.exit(f"Claude API에 연결할 수 없습니다: {e}\nANTHROPIC_API_KEY를 설정하거나 --fake로 실행하세요.")
    debug_enabled = a.debug
    engine = Engine(load_scenario(a.scenario), ai, max_calls=a.max_calls)
    threading.Thread(target=loop, args=(engine.step, 1.0), daemon=True).start()
    threading.Thread(target=loop, args=(engine.pump, 0.1), daemon=True).start()
    print(f"http://127.0.0.1:{a.port}" + ("  (가짜 AI)" if a.fake else ""), flush=True)
    ThreadingHTTPServer(("127.0.0.1", a.port), Handler).serve_forever()


if __name__ == "__main__":
    main()

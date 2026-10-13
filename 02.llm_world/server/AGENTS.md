<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-10-13 | Updated: 2026-10-13 -->

# server

## Purpose
FastAPI 서버. 월드 상태의 유일한 원본이며, 월드 틱 루프·NPC 판단(uzu + Qwen 3.5 0.8B)·WebSocket(`/ws`) 전송·`../frontend/` 정적 서빙을 맡는다. 설계는 `../docs/notes/01.architecture.md`.

## Key Files

| File | Description |
|------|-------------|
| `README.md` | 역할·스택·모델 요약, 실행 방법 |
| `main.py` | FastAPI 앱: 맵·장소, BFS, `World`(엔티티·이동·NPC 경로), 틱 루프, NPC 판단 루프(`decide`), `/ws`, `../frontend/` 정적 서빙 |
| `llm.py` | LLM 호출 유일 지점: uzu 엔진 로드, `ask(system, user)` (lock, 매번 `reset()`) |
| `smoke_llm.py` | uzu + Qwen 0.8B 스모크 (지연·형식 확인) |
| `pyproject.toml` | uv 의존성 (uzu, fastapi) |

## For AI Agents

### Working In This Directory
- 의존성은 `uv`로 이 폴더의 `pyproject.toml`에만.
- LLM 호출은 한 모듈의 한 함수에서만. 모델 인스턴스가 하나이므로 호출은 한 번에 하나씩.
- 월드 틱은 LLM을 기다리지 않는다.
- LLM 출력 파싱 실패 → `wait`, 원문 로그. 서버가 죽으면 안 된다.
- 프로토콜을 바꾸면 `../docs/notes/01.architecture.md` "프로토콜" 절도 고친다.

### Testing Requirements
- `uv run`으로 서버를 띄우고 브라우저로 확인. 테스트는 요청 시에만.

### Common Patterns
- uzu 0.6.3 `Grammar`는 무시된다. 출력 형식은 프롬프트 `Format:` 줄 + 서버의 관대한 파싱(선택지 이름 검색)으로.
- 무효 응답은 랜덤으로 대체하지 않는다 — 로그에 `INVALID`로 남기고 재시도.

<!-- MANUAL: -->

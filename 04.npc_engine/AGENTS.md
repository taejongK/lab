<!-- Generated: 2026-10-25 | Updated: 2026-11-05 -->

# 04.npc_engine

## Purpose
AI가 게임 마스터와 NPC를 맡는 2D TRPG 엔진 실험. 질문/상태/날짜/결론은 `README.md` 참조.

## Key Files

| File | Description |
|------|-------------|
| `.env.example` | OpenRouter 키·모델 설정 틀. 실제 값은 `.env`(커밋 안 됨) |
| `README.md` | 실험 질문·상태·시작일·최종 수정일·결론, 문서 목록 |
| `CLAUDE.md` | 이 실험의 자동 문서화 규칙 (worklog-discipline + 문서 위치) |
| `probe_ascii_map.py` | ASCII 2D 맵에서 로컬 Laya가 이동 방향·목표 오브젝트를 고를 수 있는지 측정 (`uv run probe_ascii_map.py 60 20`) |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `src/` | 엔진 코드: `world.py`(규칙), `engine.py`(흐름), `ai.py`(OpenRouter), `fake_ai.py`, `server.py`, `playtest.py`, `web/`(`home.html` 홈, `index.html` 게임, `create.html` 창작자 페이지) |
| `scenarios/` | 시나리오 파일과 도트 데이터(`*.sprites.json`). `_blank*`는 새 게임 틀. 엔진 코드에 시나리오 전용 처리를 넣지 않는다 |
| `docs/notes/` | 직접 작성한 스터디 문서 (번호 붙인 `NN.주제.md`) |
| `docs/reference/` | 외부 자료 — 링크 모음, 받아 둔 원문 |
| `docs/worklog/` | 날짜별 작업 기록 |
| `docs/plan/` | 기능 계획 / devlog / 인계 문서 |
| `docs/report/` | 조사·실험 보고서 (md, 설계 문서 html) |

## For AI Agents

### Working In This Directory
- lab 저장소 규칙을 따른다: 다른 최상위 실험 폴더에서 import 금지, 의존성은 이 폴더 안에서만.
- 기본은 버려도 되는 코드. 테스트/추상화는 명시적 요청 시에만.

### Testing Requirements
- 스크립트 직접 실행으로 동작 확인 (Python은 PEP 723 + `uv run`). 엔진 변경 후 `uv run src/playtest.py`.

### Common Patterns
- AI는 세계를 직접 바꾸지 않는다. `World.apply()`를 통과한 변경만 적용한다.
- 캐릭터에게는 자기 메모리와 주변만 준다. 세계 전체는 게임 마스터에게만 준다.

<!-- MANUAL: -->
<!--
  이 마커 아래 내용은 AGENTS.md 재생성(/sync-agents) 시 보존된다.
  자동 생성이 덮어쓰지 못하는 손으로 쓴 맥락을 여기에 남긴다.
-->

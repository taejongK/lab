<!-- Generated: 2026-10-13 | Updated: 2026-10-13 -->

# 02.llm_world

## Purpose
2D 월드에서 상호작용을 통해 자유롭게 이동하는 LLM NPC를 만든다. 프론트(`frontend/`)와 서버(`server/`)를 분리해 구성한다. 질문/상태/날짜/결론은 `README.md` 참조.

## Key Files

| File | Description |
|------|-------------|
| `README.md` | 실험 질문·상태·시작일·최종 수정일·결론, 문서 목록 |
| `CLAUDE.md` | 자동 문서화 규칙 + 개발 규칙(스택·역할 경계·프로토콜·LLM 출력) |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `frontend/` | 2D 월드 렌더링·플레이어 입력 (도트 스타일 Canvas 2D) (see `frontend/AGENTS.md`) |
| `server/` | 월드 상태·NPC 에이전트 (FastAPI + uzu, Qwen 3.5 0.8B) (see `server/AGENTS.md`) |
| `docs/notes/` | 직접 작성한 스터디 문서 (번호 붙인 `NN.주제.md`) |
| `docs/reference/` | 외부 자료 — 링크 모음, 받아 둔 원문 |
| `docs/worklog/` | 날짜별 작업 기록 |
| `docs/plan/` | 기능 계획 / devlog / 인계 문서 |

## For AI Agents

### Working In This Directory
- lab 저장소 규칙을 따른다: 다른 최상위 실험 폴더에서 import 금지, 의존성은 이 폴더 안에서만.
- 기본은 버려도 되는 코드. 테스트/추상화는 명시적 요청 시에만.

### Testing Requirements
- 서버(`server/`, `uv run`)를 띄우고 브라우저로 직접 확인.

### Common Patterns
- 설계 기준: `docs/notes/01.architecture.md`. 진행 상황: `docs/plan/active/20261013_mvp_devlog.md`.

<!-- MANUAL: -->
<!--
  이 마커 아래 내용은 AGENTS.md 재생성(/sync-agents) 시 보존된다.
  자동 생성이 덮어쓰지 못하는 손으로 쓴 맥락을 여기에 남긴다.
-->

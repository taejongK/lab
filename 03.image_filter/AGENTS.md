<!-- Generated: 2026-10-19 | Updated: 2026-10-19 -->

# 03.image_filter

## Purpose
(작성 예정) 질문/상태/날짜/결론은 `README.md` 참조.

## Key Files

| File | Description |
|------|-------------|
| `README.md` | 실험 질문·상태·시작일·최종 수정일·결론, 문서 목록 |
| `CLAUDE.md` | 이 실험의 자동 문서화 규칙 (worklog-discipline + 문서 위치) |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `docs/notes/` | 직접 작성한 스터디 문서 (번호 붙인 `NN.주제.md`) |
| `docs/reference/` | 외부 자료 — 링크 모음, 받아 둔 원문 |
| `docs/worklog/` | 날짜별 작업 기록 |
| `docs/plan/` | 기능 계획 / devlog / 인계 문서 |

## For AI Agents

### Working In This Directory
- lab 저장소 규칙을 따른다: 다른 최상위 실험 폴더에서 import 금지, 의존성은 이 폴더 안에서만.
- 기본은 버려도 되는 코드. 테스트/추상화는 명시적 요청 시에만.

### Testing Requirements
- 스크립트 직접 실행으로 동작 확인 (Python은 PEP 723 + `uv run`).

### Common Patterns
- (아직 없음)

<!-- MANUAL: -->
<!--
  이 마커 아래 내용은 AGENTS.md 재생성(/sync-agents) 시 보존된다.
  자동 생성이 덮어쓰지 못하는 손으로 쓴 맥락을 여기에 남긴다.
-->

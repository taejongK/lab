<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-10-13 | Updated: 2026-10-13 -->

# frontend

## Purpose
도트 스타일 2D 월드를 Canvas 2D로 그리고 플레이어 입력을 서버로 보낸다. 상태는 전부 서버(`/ws`)에서 받는다. 설계는 `../docs/notes/01.architecture.md`.

## Key Files

| File | Description |
|------|-------------|
| `README.md` | 역할·스택 요약 |

## For AI Agents

### Working In This Directory
- 순수 HTML/JS만. npm·번들러·프레임워크 금지.
- 게임 로직(충돌·이동 판정·NPC 판단) 금지. 받은 상태를 그리고 입력을 보내기만 한다.
- 도트 렌더링: 정수배 확대, `ctx.imageSmoothingEnabled = false`.
- 메시지 형식은 `../docs/notes/01.architecture.md`의 "프로토콜" 절을 따른다.

### Testing Requirements
- 서버를 띄우고(FastAPI가 이 폴더를 `/`에 서빙) 브라우저에서 직접 확인.

### Common Patterns
- (아직 없음)

<!-- MANUAL: -->

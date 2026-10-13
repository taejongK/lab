# CLAUDE.md

<!-- worklog-discipline:auto-doc-rules v0.1.0 -->
<!-- 이 블록은 worklog-discipline 플러그인의 /init-workstructure 가 주입한다. 통째로 교체/갱신되므로 이 마커 사이를 직접 편집하지 말 것. -->

## 자동 문서화 규칙 (필수)

작업과 함께 문서를 갱신한다. 아래 상황에서는 **사용자가 요청하지 않아도 자동으로** 실행한다.

### 작업 완료 시 (Worklog) — 항상

```
1. 작업이 끝나면 docs/worklog/{YYYY_MM_DD}.md 파일에 기록한다.
   - 파일이 없으면 생성, 있으면 해당 날짜 파일에 작업별로 append.
   - 파일명 형식: YYYY_MM_DD.md (예: 2026_07_10.md)

2. 각 작업 항목에 반드시 포함:
   - 작업자 이름 (모르면 사용자에게 물어본다)
   - 대상 파일/모듈
   - 무엇을·왜 변경했는지, 검증 방법/결과

3. 헤더 최소화 — 헤더를 여러 단계로 쓰지 않는다.
   각 작업 항목 제목만 `###`로 구분하고, 항목 내부 구분(배경/방법/결과/검증 등)은
   별도 헤더 대신 볼드 라벨·불렛으로 가볍게 표현한다.
```

### 기능 개발 시작 시 (devlog)

```
docs/plan/templates/DEV_LOG_TEMPLATE.md 를 복사해
docs/plan/active/{YYYYMMDD}_{기능명}_devlog.md 생성:
- 기능명·목표·완료 기준을 채우고 초기 개발 계획을 작성한다.
```

### 개발 중 방향/결정 변경 시 (devlog 갱신)

```
docs/plan/active/{기능명}_devlog.md 갱신:
- 변경 이력 테이블에 날짜·변경 내용·이유를 추가한다.
- 현재 상태 섹션(마지막 작업/다음 할 일)을 갱신한다.
```

### 기능 구현 완료 시 (인계 문서)

```
docs/plan/templates/HANDOVER_TEMPLATE.md 를 복사해
docs/plan/active/{YYYYMMDD}_{기능명}.md 생성:
- 핵심 구현 로직, 데이터 흐름, 설계 결정, 구현 시 주의사항을 채운다.
docs/plan/handover-index.md 의 인계 대기 테이블에 추가한다.
```

### 인계 완료 시

```
docs/plan/active/{기능명}.md 와 {기능명}_devlog.md 를 docs/plan/completed/ 로 이동.
docs/plan/handover-index.md 의 인계 현황 테이블을 갱신한다.
```

### 디렉터리 구조 변경 시 (AGENTS.md 계층)

```
새 디렉터리 추가/역할 변경 시 해당 디렉터리의 AGENTS.md 를 갱신한다.
- 상위 디렉터리 AGENTS.md 의 Subdirectories 표도 함께 갱신.
- <!-- MANUAL: --> 마커 아래 손으로 쓴 내용은 절대 덮어쓰지 않는다.
- 없으면 docs/plan/templates/AGENTS_TEMPLATE.md 형식으로 새로 만든다.
```

### 프로젝트별 확장 규칙 (Extension)

> 이 프로젝트 고유의 자동 문서화 규칙(예: 모델 레지스트리, API 레퍼런스, 스키마 변경 로그)은
> 아래에 추가한다. 위 코어 규칙은 플러그인이 갱신 시 교체하지만, 이 확장 절은 건드리지 않는다.

<!-- PROJECT-EXTENSIONS: 아래에 프로젝트 고유 규칙을 적는다 -->

#### 문서 위치

모든 문서는 `docs/` 아래에 둔다. 폴더 루트에는 `README.md`, `CLAUDE.md`, `AGENTS.md`와 코드만 남긴다.

| 위치 | 넣는 것 |
|---|---|
| `docs/notes/` | 직접 작성한 스터디 문서. 파일명은 `NN.주제.md` (01부터 번호) |
| `docs/reference/` | 외부 자료. `README.md`에 링크를 모으고, 원문 파일을 받으면 여기에 둔다 |
| `docs/worklog/` | 위 Worklog 규칙 |
| `docs/plan/` | 위 devlog / 인계 규칙 |

- `docs/notes/`에 문서를 추가하면 `README.md`의 문서 표에도 한 줄 추가한다.
- 이 폴더의 파일을 바꾸면 `README.md`의 **최종 수정일**을 오늘 날짜로 갱신한다.

#### 개발 규칙

설계 기준 문서는 `docs/notes/01.architecture.md`. 코드와 어긋나면 둘 중 하나를 고치고 같이 커밋한다.

**스택 (확정 — 바꾸려면 먼저 사용자에게 묻고 devlog 변경 이력에 남긴다)**
- 프론트: HTML5 Canvas 2D + 순수 JS. npm·번들러·프레임워크 금지. 도트 스타일(정수배 확대, `imageSmoothingEnabled = false`).
- 서버: FastAPI, `uv`로 의존성 관리 (`server/pyproject.toml`).
- 통신: WebSocket 하나 (`/ws`).
- LLM: uzu Python 바인딩, 모델 `alibaba:qwen3.5:0.8b:mirai:mirai-m:4`.

**역할 경계**
- 서버가 월드 상태의 유일한 원본이다. 프론트는 받은 상태를 그리고 입력을 보내기만 한다. 충돌 판정·이동·NPC 판단을 프론트에 두지 않는다.
- LLM 호출은 `server/` 안의 한 곳에서만 한다. 다른 모듈은 그 함수를 통해서만 부른다.

**프로토콜**
- WebSocket 메시지 형식을 바꾸면 `docs/notes/01.architecture.md`의 "프로토콜" 절을 같은 작업에서 고친다.

**LLM 출력**
- 모델이 작다(0.8B). 출력이 형식을 어겨도 서버가 죽지 않게 한다. 파싱 실패 → `wait` 행동으로 처리하고 원문을 로그로 남긴다.
- 프롬프트를 바꾸면 devlog 변경 이력에 이유와 함께 남긴다 (행동 품질이 프롬프트에 크게 좌우되므로).

**커밋하지 않는 것**
- 모델 가중치·캐시, `.venv/`, API 키. 에셋은 라이선스(CC0 등)를 `docs/reference/README.md`에 적은 것만 커밋한다.

**동작 확인**
- 서버를 띄우고 브라우저로 직접 확인한다. 테스트는 요청 시에만.

<!-- /worklog-discipline:auto-doc-rules -->

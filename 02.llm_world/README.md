# LLM World

- 질문: 2D 월드에서 LLM이 조종하는 NPC가 플레이어·다른 NPC·오브젝트와의 상호작용만으로 스스로 판단해 자유롭게 돌아다니게 만들 수 있는가?
- 상태: 진행중
- 시작일: 2026-10-13
- 최종 수정일: 2026-10-13
- 결론: (아직 없음)

## 목표

1. **2D 월드**: 타일/그리드 기반 맵에 플레이어와 NPC 여러 명이 있고, 브라우저에서 실시간으로 보인다.
2. **LLM NPC 이동**: NPC는 정해진 경로가 아니라 LLM이 주변 상황(위치, 근처 대상, 최근 대화)을 보고 다음 행동(이동 목적지·대화·대기)을 고른다.
3. **상호작용**: 플레이어가 NPC에게 말을 걸거나 NPC끼리 마주치면 대화가 일어나고, 그 결과가 이후 이동에 영향을 준다.
4. **프론트/서버 분리**: 월드 상태와 NPC 판단은 서버가, 렌더링과 입력은 프론트가 맡는다.

### 완료 기준 (MVP)

> **MVP의 판정 질문은 하나다: LLM 판단만으로 NPC가 스스로 목적지를 골라 이동하는가?**
> 대화·에셋·기억은 이 질문을 확인하는 데 필요한 최소한만 만든다. 품질·연출은 MVP 이후.


- 맵 1개, NPC 2명 이상, 플레이어 1명이 한 화면에서 움직인다.
- 플레이어 입력 없이 두어도 NPC가 LLM 판단으로 이동·대화를 이어간다.
- 플레이어가 NPC에게 한 말이 그 NPC의 다음 행동에 반영되는 것을 로그로 확인할 수 있다.

### 범위 밖 (지금은)

- 멀티플레이어, 계정, 영속 저장(DB), 아트 에셋 퀄리티, 배포.

## 구성

| 폴더 | 역할 |
|---|---|
| [frontend/](frontend/) | 2D 월드 렌더링, 플레이어 입력, 서버와 실시간 통신 |
| [server/](server/) | 월드 상태·틱 루프, NPC 에이전트(LLM 호출), 프론트에 상태 전달 |

## 스택

| 영역 | 선택 | 상태 |
|---|---|---|
| 렌더링 | HTML5 Canvas 2D, 도트(픽셀아트) 스타일 — 16×16 타일·스프라이트를 정수배 확대, `imageSmoothingEnabled = false` | 확정 |
| 서버 | FastAPI (Python, `uv`) | 확정 |
| 프론트↔서버 | WebSocket (FastAPI 내장 지원) | 확정 |
| LLM 런타임 | [uzu](https://github.com/trymirai/uzu) (Rust 엔진, Python 바인딩 `uzu==0.6.3`, Apple Silicon Metal) | 확정 |
| 모델 | Qwen 3.5 0.8B (`alibaba:qwen3.5:0.8b:mirai:mirai-m:4`, uzu가 자동 다운로드) | 확정 |
| 모델 (나중에) | `gemma-4-e4b-it` — 미리 변환된 목록에 없어 [lalamo](https://github.com/trymirai/lalamo)로 `google/gemma-4-E4B-it` 변환 필요 | 보류 |

## 문서

직접 쓴 문서는 `docs/notes/`에, 외부 자료는 `docs/reference/`에 둔다.

| 파일 | 내용 |
|---|---|
| [docs/notes/01.architecture.md](docs/notes/01.architecture.md) | MVP 아키텍처: 서버 루프, NPC 판단, WebSocket 프로토콜 (초안) |
| [docs/plan/active/20261013_mvp_devlog.md](docs/plan/active/20261013_mvp_devlog.md) | MVP 개발 계획·진행 상황·결정 사항 |
| [docs/reference/](docs/reference/) | 외부 자료 링크 모음 (uzu, lalamo) |

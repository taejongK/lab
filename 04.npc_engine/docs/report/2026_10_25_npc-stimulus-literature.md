# 외부 자극에 반응하는 AI NPC — 최근 3년 자료 조사

## 목적

- 외부 자극(플레이어 행동·환경 변화·소리·시야)에 반응해 동작하는 AI NPC를 만들기 전에, 2023-10 ~ 2026-10 자료를 모아 설계 축을 잡는다.

## 방법

- arXiv·공식 문서·업계 발표를 웹 검색으로 수집
- arXiv 논문은 arXiv API로 제목·게시일·초록을 직접 확인 → [초록 원문](../reference/npc-papers_arxiv-abstracts.md)
- 기간 밖이지만 거의 모든 후속 연구가 기반으로 삼는 논문은 "배경"으로 따로 표시

## 결과

### 1. 서베이 (출발점)

| 자료 | 시기 | 요점 |
|---|---|---|
| [LLMs and Games: A Survey and Roadmap](https://arxiv.org/abs/2402.18659) | 2024-02 | 게임 안 LLM의 역할 분류. 배경 NPC·전경 NPC 행동을 게임 규칙에 grounding 하는 문제 제기 |
| [A Survey on LLM-Based Game Agents](https://arxiv.org/abs/2404.02039) | 2024-04 (2025 개정) | 메모리·추론·perception-action 인터페이스로 정리. 장르별로 요구 지연시간이 다름 (액션 = 저지연 제어) |

### 2. 자극 → 판단 구조 (아키텍처)

| 자료 | 시기 | 자극 반응 관점의 요점 |
|---|---|---|
| [Generative Agents](https://arxiv.org/abs/2304.03442) (배경) | 2023-04 | 관찰 → 메모리 스트림 → 반성 → 계획. 관찰 시 "반응할지" 판단 후 계획 수정. 대부분 후속 연구의 기준선 |
| [Lyfe Agents](https://arxiv.org/abs/2310.02172) (경계, 2023-10-03) | 2023-10 | option-action 구조 + 비동기 self-monitoring + Summarize-and-Forget 메모리. 실시간 반응을 위해 LLM 호출 수를 줄임. 비용 10~100배 절감 주장 |
| [Humanoid Agents](https://arxiv.org/abs/2310.05418) (경계, 2023-10-08) | 2023-10 | 욕구·감정·관계 친밀도(System 1 요소)를 추가. 행동 후 욕구·감정 변화를 평가해 계획 갱신 |
| [Affordable Generative Agents](https://arxiv.org/abs/2402.02053) | 2024-02 | 반복되는 환경 상호작용은 LLM 대신 학습된 정책으로 대체 → 비용 절감 |
| [Concordia](https://arxiv.org/abs/2312.03664) / [v2](https://arxiv.org/abs/2507.08892) | 2023-12 / 2025-07 | Game Master가 환경을 맡아 행동의 물리적 타당성 판정, 결과를 관찰로 돌려줌. v2는 Entity-Component 패턴 |
| [Project Sid (PIANO)](https://arxiv.org/abs/2411.00114) | 2024-10 | 여러 모듈을 병렬로 돌리고 결과를 모아 행동·발화를 일관되게 유지. 10~1000+ 에이전트 |
| [LLM Reasoner + Automated Planner](https://arxiv.org/abs/2501.10106) | 2025-01 | LLM이 목표 선택, 고전 플래너(Fast Downward)가 행동 순서 생성. 새 지각마다 world state 갱신 후 재계획 |
| [MiniAgentPro](https://arxiv.org/abs/2509.13011) | 2025-09 | 생성 에이전트의 이벤트 조직·협력 평가 + 맵 에디터 시각화 플랫폼 |

### 3. LLM → 실행 가능한 행동 (BT / 코드)

| 자료 | 시기 | 요점 |
|---|---|---|
| [Free-Form Text Command → Behavior Branch](https://arxiv.org/abs/2402.07442) | 2024-02 | 자연어 명령을 LLM 코드 생성으로 behavior tree 가지(behavior branch)로 변환 |
| [PORTAL: Agents Play Thousands of 3D Games](https://arxiv.org/abs/2503.13356) | 2025-03 | LLM이 BT를 DSL로 생성. 매 프레임 LLM 호출 대신 정책(BT)을 만들어 둠 |
| [Voyager](https://arxiv.org/abs/2305.16291) (배경) | 2023-05 | 환경 피드백을 반영하는 반복 프롬프팅 + 실행 가능한 스킬 코드 라이브러리 (Minecraft) |

### 4. 지각 (환경을 어떻게 입력할지)

| 자료 | 시기 | 요점 |
|---|---|---|
| [NPC Dialogue with Panoramic Images](https://arxiv.org/abs/2604.19192) | 2026-04 | NPC 주변 파노라마 + semantic segmentation → 주변 물체·랜드마크를 대화에 반영. "환경 변화에 무지한 NPC" 문제를 직접 다룸 |
| [SIMA](https://arxiv.org/abs/2404.10179) / [SIMA 2](https://deepmind.google/sima) | 2024-03 / 2025-11 | 화면 픽셀 + 언어 지시 → 키보드·마우스 행동. SIMA 2는 Gemini 기반, 다단계 계획. SIMA 2 내용은 블로그·기사 기준 (논문 미확인) |
| [ReactiveGWM](https://arxiv.org/abs/2605.15256) | 2026-05 | 게임 world model 안에서 플레이어 행동에 NPC가 반응하도록 생성. 엔진 NPC가 아니라 영상 생성 쪽 접근 |

### 5. 실시간성 (지연 문제)

| 자료 | 시기 | 요점 |
|---|---|---|
| [The Latent Bridge](https://arxiv.org/abs/2606.24470) | 2026-06 | 느린 추론 VLM(~1.5s/응답)과 빠른 반응 VLM을 잇는 slow-fast 구조. 15Hz 제어 루프 대상 |
| [Speculative Interaction Agents](https://arxiv.org/abs/2605.13360) | 2026-05 | 비동기 I/O + 추측성 tool call로 대화형 에이전트 지연 감소. NPC 전용은 아님 |

### 6. 평가·사용자 연구

| 자료 | 시기 | 요점 |
|---|---|---|
| [AI NPC Realism in VR](https://arxiv.org/abs/2507.10469) | 2025-07 | GPT-4 Turbo NPC 2명 VR 심문 시뮬레이터. 믿음직함 6.67/10 (2차 인용 기준), 지연이 주요 과제 |
| [LLM-NPC와 인지 부하](https://arxiv.org/abs/2604.10107) | 2026-04 | N=130 무작위 실험, LLM-NPC vs 스크립트 NPC. 개방형 상호작용의 양면성 |
| [Generative Agent Simulations of 1,000 People](https://arxiv.org/abs/2411.10109) | 2024-11 | 실제 인터뷰 기반 에이전트가 개인 응답을 재현. NPC 성격 grounding 참고용 |
| [Orchestrated Reality](https://arxiv.org/abs/2606.16014) | 2026-06 | LLM 월드 시뮬레이션을 parameterized-action POMDP로 정식화. 상태 추적 + 서사 결합 |

### 7. 업계 사례

| 자료 | 시기 | 요점 |
|---|---|---|
| [NVIDIA ACE 자율 캐릭터](https://www.nvidia.com/en-eu/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/) | 2025-01 (CES) | 대화형 NPC → 지각·계획·행동. 소형 LM(계획) + 멀티모달(시각·청각). PUBG Ally, inZOI Smart Zoi |
| [NVIDIA In-Game Inference SDK](https://developer.nvidia.com/blog/bring-nvidia-ace-ai-characters-to-games-with-the-new-in-game-inference-sdk) | 2025 | 온디바이스 추론으로 지각·계획·실행 |
| [Inworld Goals / Triggers](https://docs.inworld.ai/docs/tutorial-basics/goals) | 상시 | 트리거(게임 이벤트) 또는 대화 intent → goal 활성화 → 행동. "자극 → 반응" 매핑을 데이터로 정의하는 실용 패턴 |
| [Mantella (Skyrim/Fallout 4 mod)](https://github.com/art-from-the-machine/Mantella) | 2023~ | STT + LLM + TTS. 시간대·소지품 등 게임 상태를 프롬프트에 주입 |

## 해석

- 공통 구조: 지각(이벤트·관찰) → 반응 여부 판단 → 계획/행동 선택 → 실행 → 결과를 다시 관찰.
- 가장 큰 제약은 지연. 대응은 세 갈래:
  - LLM 호출 줄이기: 반응 필요 여부를 먼저 거르기 (Lyfe, Affordable)
  - LLM은 느린 층에서 목표·정책만 정하고, 빠른 층(BT·플래너·정책)이 실행 (PORTAL, LLM+Planner, Latent Bridge, NVIDIA ACE)
  - 병렬·비동기 처리 (PIANO, Speculative)
- 지각 입력: 텍스트 이벤트(대부분 연구·Inworld 트리거) vs 시각(파노라마, SIMA). 처음 만들 때는 텍스트 이벤트가 압도적으로 싸다.
- 처음 만들 출발점으로는 "이벤트 큐 → 규칙/BT 즉시 반응 + LLM 느린 판단" 2층 구조가 위 자료와 가장 잘 맞는다.

## 남은 질문

- 반응 대상 자극의 범위 (소리·시야·플레이어 발화·월드 이벤트 중 무엇부터?)
- 실행 환경 (텍스트 시뮬레이션 / Unity·Godot / 기존 게임 mod)
- 로컬 소형 모델 vs API 모델 — 허용 지연시간 기준
- 감정·욕구 모델(Humanoid Agents류)을 넣을지

## 출처

- 본문 표의 링크가 출처. arXiv 초록 원문: [npc-papers_arxiv-abstracts.md](../reference/npc-papers_arxiv-abstracts.md)
- 2차 자료만 확인한 것: SIMA 2(블로그·기사), VR 실험의 6.67/10 수치(검색 요약), ACE 탑재 게임의 실제 출시 상태(미확인)

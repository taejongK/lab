# AgeMem 논문 분석 — 장기·단기 메모리를 한 정책으로 RL 학습

- 논문: Yu et al., *Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents* — [arXiv:2601.01885](https://arxiv.org/abs/2601.01885) (v3, 2026-07-23 기준으로 읽음) · [초록 원문](../reference/papers/agemem_arxiv-2601.01885.md)
- 소속: Wuhan University, Alibaba Group
- 학회: ACL 2026 SAC Highlight (arXiv 코멘트 기준, 학회 페이지는 확인 안 함)
- 코드: [github.com/y1y5/AgeMem](https://github.com/y1y5/AgeMem) (AgentScope + Trinity-RFT 기반. 저장소 존재만 확인, 실행은 안 함)

## 목적

- 이 프로젝트의 6번 카테고리 "RL로 학습된 메모리 관리"([01 노트](../notes/01.memory-architecture-patterns.md))에 새로 나온 논문 하나를 자세히 읽는다.
- 기존에 모은 Memory-R1·MEM1·Mem-α와 무엇이 다른지, 주장하는 수치가 무엇을 근거로 하는지 확인한다.

## 방법

- arXiv PDF v3 전문(본문 + 부록 A~D)을 읽고 표·식 수치를 그대로 옮김.
- 비교 대상 논문은 [papers/](../reference/papers/README.md)에 받아 둔 초록 기준. 그쪽 본문 수치는 확인하지 않음.
- "해석" 절의 비판은 논문 수치에서 계산한 것과 내 추론을 구분해 적음.

## 결과

### 1. 한 줄 요약

장기 메모리(LTM) 조작 3개와 단기 컨텍스트(STM) 조작 3개를 전부 에이전트의 도구로 열어 두고, 한 LLM이 언제 무엇을 쓸지를 GRPO로 끝까지(end-to-end) 학습시킨다. 별도 메모리 매니저 모델이 없다. ([§3](https://arxiv.org/abs/2601.01885))

### 2. 문제 제기

기존 구조를 두 가지로 나눈다 (Figure 1).

| 구조 | STM | LTM | 예 |
|---|---|---|---|
| (a) | 고정 (RAG·주기적 요약) | 정해진 시점에 저장 (trigger-based) | Mem0, MemoryBank |
| (b) | 고정 | 별도 매니저가 결정 (agent-based) | Memory-R1, A-Mem |
| (c) AgeMem | 에이전트가 도구로 조작 | 에이전트가 도구로 조작 | — |

논문이 짚는 어려움 세 가지:

- C1 기능 이질성: LTM은 "무엇을 저장·갱신·삭제"하고, STM은 "무엇을 꺼내·요약·버릴지"를 다룬다. 이 둘을 한 메커니즘으로 조율해야 함.
- C2 학습 방식 불일치: LTM 학습은 세션 정보를 미리 주고, STM 학습은 방해 문장을 넣어 길게 만든다. 또 메모리 조작은 보상이 맨 끝에만 나와 궤적이 끊긴다.
- C3 배포 비용: 메모리 전용 보조 LLM을 두면 추론·학습 비용이 늘어남.

### 3. 도구 6개 (Table 1, 부록 A.1)

| 도구 | 대상 | 동작 |
|---|---|---|
| ADD | LTM | 내용 + 임베딩 + 메타데이터(시각·출처·태그)로 새 항목 추가 |
| UPDATE | LTM | `memory_id`로 기존 항목 내용 교체 (id는 이전 검색 결과에서 얻음) |
| DELETE | LTM | `memory_id` + `confirmation=true`로 삭제 |
| RETRIEVE | LTM → STM | 코사인 유사도 top-k(보통 3~5)를 컨텍스트에 삽입. 메타데이터 필터 가능 |
| SUMMARY | STM | 최근 N 라운드 또는 전체를 LLM 요약으로 교체 |
| FILTER | STM | 기준 문장과 유사도가 θf(기본 0.6) 이상인 메시지를 컨텍스트에서 제거 |

- 출력 형식: `<think>` 다음에 `<tool_call>`(JSON 배열, 여러 개 가능) 또는 `<answer>` 중 하나만.
- RETRIEVE를 표에서는 STM 도구로 분류함. "LTM에서 꺼내 컨텍스트로 옮기는 일"을 컨텍스트 관리로 본 것.

### 4. 학습: 3단계 궤적 (§3.1, §3.3)

한 학습 예제를 세 구간으로 이어 붙인 하나의 궤적으로 만든다.

| 단계 | 에이전트가 받는 것 | 배우는 것 | 상태 처리 |
|---|---|---|---|
| Stage 1 | 일상 대화 속에 섞인 맥락 정보 Iq (HotpotQA supporting facts) | 질문을 모른 채 쓸모 있을 정보를 LTM에 저장 | 매 스텝 RETRIEVE로 현재 LTM 내용 확인 |
| Stage 2 | 질문과 무관한 방해 발화 N개(기본 5, DistractorGen이 외부 LLM으로 생성) | FILTER·SUMMARY로 컨텍스트 정리 | STM 리셋, LTM 유지 |
| Stage 3 | 실제 질문 q | LTM 검색 + 컨텍스트 관리 + 답변 | — |

- Stage 2 전에 STM을 비우므로, Stage 3에서 답하려면 Stage 1에서 LTM에 잘 넣어 둔 것을 꺼내야만 함. 저장 결정이 나중 성적에 직접 묶이는 구조.
- 저자 주장: 이 구조는 QA 전용이 아니라 "정보 노출 → 방해 → 과제"의 시간 분리만 있으면 됨 (§3.3). 실제 학습은 HotpotQA로만 했음.

### 5. Step-wise GRPO (§3.4)

- 같은 질문으로 K=8개 궤적을 굴리고, 마지막 보상을 그룹 평균·표준편차로 정규화해 advantage를 구함.
- 그 advantage를 궤적의 모든 스텝(Stage 1의 ADD, Stage 2의 FILTER 포함)에 똑같이 붙임 → 최종 성적이 초반 메모리 결정까지 감독.
- KL 계수 β=0.1, 최대 컨텍스트 8,192 토큰, 응답 2,048 토큰, RTX 4090 48GB × 8.

### 6. 보상 (§3.5, 부록 A.2)

R = (1/3)·R_task + (1/3)·R_context + (1/3)·R_memory + 페널티

| 항목 | 구성 (각 하위 항목 가중치 1/3) |
|---|---|
| R_task | LLM 심판 점수 [0,1]. 답이 없으면 −1 |
| R_context | 압축률 max(0, 1 − 사용 토큰/한도) · 넘치기 전에 요약·필터를 불렀는가(0/1) · 질문 핵심어가 답할 때 컨텍스트에 남아 있는가(0/1) |
| R_memory | 저장 품질 = LLM이 고품질로 판정한 항목 비율 · 갱신/삭제를 한 번이라도 했는가(0/1) · 검색된 기억과 질문의 LLM 관련도 |
| 페널티 | 라운드 초과 −1, 토큰 한도 초과 −0.5 |

### 7. 주요 수치

평가: ALFWorld·SciWorld·BabyAI는 성공률, PDDL은 진행률, HotpotQA는 LLM 심판 점수. 학습은 HotpotQA로만 하고 나머지 4개는 그대로 평가. (Table 2)

| 백본 | No-Memory | 최고 기준선 | AgeMem-noRL | AgeMem |
|---|---|---|---|---|
| Qwen2.5-7B-Instruct 평균 | 28.05 | 37.14 (Mem0) | 33.43 | 41.96 |
| Qwen3-4B-Instruct 평균 | 43.97 | 45.74 (A-Mem) | 45.59 | 54.31 |

- 최고 기준선 대비 +4.82 / +8.57 %p, RL 유무 차이 +8.53 / +8.72 %p.
- 기억 품질 MQ(HotpotQA 정답 근거 문장과 저장된 기억의 관련도, LLM 평가): 0.533 / 0.605로 최고 (Figure 2).
- 프롬프트 토큰: STM 도구 대신 RAG를 쓴 변형 대비 −3.1%(2,186→2,117) / −5.1%(2,310→2,191) (Figure 3).
- RL 후 도구 사용 변화 (Table 3, 7B): ADD 0.92→1.64, UPDATE 0→0.13, DELETE 0→0.08, FILTER 0.02→0.31, RETRIEVE 2.31→1.95.
- 보상 절제 (Table 4·6): 답 점수만 쓰면 7B J 0.509 / MQ 0.479, 전체 보상이면 0.544 / 0.533. 4B는 J 0.546→0.555, MQ 0.415→0.605.
- FILTER 임계값 θf 0.4~0.8, 방해 발화 수 N 3~7에서 J 0.52~0.55로 안정 (Table 5·8).

### 8. "통합"의 순수 효과 — 부록 D.3

리뷰어 지적("STM 도구·RL을 붙여서 오른 것 아니냐")에 답하려고 기존 LTM 시스템에도 같은 STM 도구 + RL을 붙여 비교 (Table 7, 7B, ALFWorld·SciWorld·HotpotQA 평균).

| 방법 | 원래 | + ST/RL | AgeMem과 차이 |
|---|---|---|---|
| LangMem | 34.66 | 41.56 | −2.13 |
| A-Mem | 35.56 | 41.70 | −1.99 |
| Mem0 | 37.05 | 40.67 | −3.02 |
| AgeMem | — | 43.69 | — |

## 해석

### 새로운 점

- LTM 쓰기와 STM 정리를 같은 정책·같은 최종 보상으로 묶은 첫 시도에 가깝다. Memory-R1은 매니저와 답변 에이전트를 나눴고, MEM1은 외부 저장소 없이 내부 상태 하나만 갱신하며, Mem-α는 저장(construction)만 학습한다 ([Memory-R1](../reference/papers/memory_r1_arxiv-2508.19828.md) · [MEM1](../reference/papers/mem1_arxiv-2506.15841.md) · [Mem-α](../reference/papers/mem_alpha_arxiv-2509.25911.md) 초록 기준).
- "STM 리셋 후 LTM만 유지" 커리큘럼이 핵심 장치. 저장을 잘못하면 Stage 3에서 반드시 손해를 보게 만들어 지연 보상 학습이 가능해짐.
- 도구 6개 설계 자체가 RL 없이도 쓸 만하다: 7B에서 AgeMem-noRL(33.43)이 No-Memory(28.05)보다 +5.4%p.

| | Memory-R1 | MEM1 | Mem-α | AgeMem |
|---|---|---|---|---|
| 학습 대상 | LTM 조작 + 답변 시 기억 선별 | 내부 상태 갱신 | LTM 구성 | LTM 조작 + STM 조작 + 답변 |
| 모델 수 | 2 (매니저, 답변) | 1 | 1 | 1 |
| 외부 저장소 | 있음 | 없음 (고정 크기 상태) | 있음 (core·episodic·semantic) | 있음 (평면 벡터 저장소) |
| 컨텍스트 정리 | 학습 안 함 | 상태 교체로 대체 | 학습 안 함 | FILTER·SUMMARY 학습 |

### 수치를 볼 때 주의할 점

1. "통합" 자체의 이득은 약 2%p다 (D.3에서 계산). 최고 기준선 대비 +4.82%p 중 상당 부분은 STM 도구와 RL을 붙인 효과이고, 같은 것을 붙인 A-Mem과의 차이는 1.99%p. 분산·시드 반복이 보고되지 않아 이 2%p가 유의한지 알 수 없다.
2. RL 기반 메모리 방법과 직접 비교하지 않았다. 기준선은 LangMem·A-Mem·Mem0·Mem0g(모두 학습 없음)뿐. Memory-R1, Memory-as-Action은 관련 연구에서만 언급.
3. 컨텍스트 압박이 거의 없는 환경이다. 한도 8,192 토큰에 평균 사용량 약 2,100 토큰. STM 도구의 토큰 절감이 3~5%에 그친 것도 이 때문으로 보인다 (내 추론). 긴 대화에서의 STM 효과는 사실상 미검증.
4. 보상이 평가 지표와 겹친다 (내 해석). R_memory의 저장 품질은 "LLM이 질문·정답을 보고 고품질로 판정한 비율"이고, MQ는 "LLM이 정답 근거 문장과의 관련도를 매긴 점수"다. 둘이 거의 같은 것을 재므로 MQ 향상은 일부 학습 목표를 그대로 측정한 결과일 수 있다.
5. 도구 사용 자체에 보상이 붙어 있다. "갱신/삭제를 한 번이라도 했으면 1", "넘치기 전 요약·필터를 불렀으면 1". RL 후 UPDATE·DELETE·FILTER 빈도가 0에서 올라간 것이 학습된 판단인지, 보상을 따라간 것인지 구분되지 않는다. 다만 RETRIEVE는 줄었으므로 무조건 많이 부르게 된 것은 아님.
6. HotpotQA 하나로 학습하고 ALFWorld·PDDL 같은 다른 과제로 옮겨 평가했는데, 그 환경들에서 Stage 1에 무엇을 저장하게 했는지(에피소드 간 기억인지, 에피소드 안 기억인지) 본문에 구체적 설명이 없다. 확인 못 함.
7. 메모리가 오히려 해가 되는 경우가 있다. 7B PDDL에서 AgeMem-noRL 8.87 < No-Memory 10.15, 4B HotpotQA에서 Mem0 39.16 < No-Memory 47.48. 학습 없이 메모리 도구를 주는 것만으로는 안전하지 않다는 근거.
8. 작은 오픈 모델(4B·7B)만 실험. 큰 모델이나 상용 API 모델에서 같은 차이가 나는지는 모른다.
9. 사소한 불일치: FILTER는 기준과 "비슷한 것을 지운다"(식 15, 도구 설명 "criteria for content removal")인데 부록 본문은 기준을 "무엇을 남길지에 대한 설명"으로도 쓸 수 있다고 적음.

### 이 프로젝트에 가져올 것

- 설계 축으로 보면 쓰기·읽기·갱신/망각을 전부 "에이전트가 도구로 결정"하는 극단에 있다 ([설계 비교 보고서](2026_10_27_agent-memory-design-comparison.html)의 6축 기준).
- RL을 못 하는 상황에서도 바로 쓸 수 있는 부분:
  - 6개 도구 스키마(부록 Figure 6·7)와 `<think>` → `<tool_call>` | `<answer>` 형식 프롬프트.
  - UPDATE·DELETE가 `memory_id`를 요구하고, 그 id는 검색 결과에서만 얻게 한 구조 → 모델이 없는 항목을 지어내 갱신하는 것을 막음.
  - 단, 7번 주의점처럼 학습 없이 도구만 주면 과제에 따라 성능이 떨어질 수 있음.
- [CS 챗봇 구조 제안](2026_11_01_cs-chatbot-memory-architecture.html)과의 관계: 규정 원문은 에이전트가 고치면 안 되므로 AgeMem식 자유 UPDATE/DELETE는 사례 카드 메모리 쪽에만 해당. 상담이 길어질 때의 SUMMARY·FILTER는 상담 세션 컨텍스트 관리에 그대로 대응됨.

## 남은 질문

- 컨텍스트 한도를 실제로 넘는 긴 대화(LongMemEval·LoCoMo 같은 다중 세션)에서도 STM 도구가 이득인가? 논문은 한계 절에서 이것을 다음 과제로 남김.
- 같은 백본·같은 데이터에서 Memory-R1과 붙이면 차이는?
- 공개 코드로 D.3의 2%p 차이를 시드 여러 개로 재현할 수 있는가?
- "도구 사용 보상"을 빼고 답 점수 + 저장 품질만 줬을 때도 UPDATE·DELETE가 생겨나는가?

## 출처

- Yu et al. 2026, AgeMem — [arXiv:2601.01885](https://arxiv.org/abs/2601.01885), 코드 [github.com/y1y5/AgeMem](https://github.com/y1y5/AgeMem)
- Memory-R1 — [arXiv:2508.19828](https://arxiv.org/abs/2508.19828)
- MEM1 — [arXiv:2506.15841](https://arxiv.org/abs/2506.15841)
- Mem-α — [arXiv:2509.25911](https://arxiv.org/abs/2509.25911)
- Mem0 — [arXiv:2504.19413](https://arxiv.org/abs/2504.19413)
- A-Mem — [arXiv:2502.12110](https://arxiv.org/abs/2502.12110)
- GRPO (DeepSeekMath) — [arXiv:2402.03300](https://arxiv.org/abs/2402.03300) (논문 인용 기준, 원문 미확인)

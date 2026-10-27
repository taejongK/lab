# 에이전트 메모리 설계 비교 (논문 48편 · 구축 사례 34건)

- 작성일: 2026-10-27
- 근거 자료: [논문 목록](../reference/papers/README.md), [사례 목록](../reference/cases/README.md)
- 범위 주의: 논문은 **초록만** 읽고 썼다 (본문 미확인). 사례는 수집한 문서 원문 기준이며, 수치는 대부분 각 회사의 자체 평가다.

## 1. 목적

에이전트 메모리를 만들 때 실제로 내려야 하는 설계 결정이 무엇이고, 연구와 실서비스가 각 결정에서 어떤 선택을 하는지 비교한다.

## 2. 방법

- 자료: 2023-03 ~ 2026-05 arXiv 논문 48편 (아키텍처 28, 학습/메모리 관리 9, 서베이 6, 벤치마크 5), 제품 문서·블로그·README 34건 (상용 어시스턴트 8, 코딩 에이전트 7, 오픈소스 14, 엔지니어링 글 5). 모두 2026-10-27 수집.
- 비교 축: 서베이들이 공통으로 쓰는 축을 합쳐 6개로 정했다.
  - [Rethinking Memory](../reference/papers/survey_rethinking_memory_arxiv-2505.00675.md)의 6개 연산 (Consolidation, Updating, Indexing, Forgetting, Retrieval, Condensation)
  - [Memory in the Age of AI Agents](../reference/papers/survey_memory_age_of_agents_arxiv-2512.13564.md)의 형태(token-level / parametric / latent)와 기능(factual / experiential / working)
  - [CoALA](../reference/papers/coala_arxiv-2309.02427.md)의 semantic / episodic / procedural 구분
- 결정 축 6개: ① 무엇을 저장하나 ② 어떤 형태로 저장하나 ③ 누가·언제 쓰나 ④ 어떻게 컨텍스트로 불러오나 ⑤ 갱신·충돌·망각 ⑥ 범위·사용자 통제
- 사례 원문은 별도 패스로 시스템별 사실(저장 대상·쓰기/읽기 경로·수치)을 인용과 함께 추출하고, 핵심 인용 9개는 원문 파일에서 grep으로 재확인했다.

## 3. 결과

### 3.1 무엇을 저장하나

| 종류 | 논문 | 실서비스 |
|---|---|---|
| 사용자 사실·선호 (semantic) | [MemoryBank](../reference/papers/memorybank_arxiv-2305.10250.md), [Mem0](../reference/papers/mem0_arxiv-2504.19413.md), [MemoryOS](../reference/papers/memoryos_arxiv-2506.06326.md) | [ChatGPT](../reference/cases/chatgpt-memory_openai-help-faq.md), [Gemini](../reference/cases/gemini-memory_google-help.md), [M365 Copilot](../reference/cases/m365-copilot-memory_microsoft-techcommunity.md), [Memobase](../reference/cases/memobase_github-readme.md) |
| 과거 경험·궤적 (episodic) | [Generative Agents](../reference/papers/generative_agents_arxiv-2304.03442.md), [Reflexion](../reference/papers/reflexion_arxiv-2303.11366.md), [G-Memory](../reference/papers/g_memory_arxiv-2506.07398.md) | [Letta recall memory](../reference/cases/letta-sleep-time-compute_letta-blog.md), [Graphiti episodes](../reference/cases/graphiti_github-readme.md) |
| 절차·전략·스킬 (procedural / experiential) | [Voyager](../reference/papers/voyager_arxiv-2305.16291.md), [AWM](../reference/papers/agent_workflow_memory_arxiv-2409.07429.md), [Memp](../reference/papers/memp_arxiv-2508.06433.md), [ReasoningBank](../reference/papers/reasoningbank_arxiv-2509.25140.md), [ACE](../reference/papers/ace_arxiv-2510.04618.md), [Dynamic Cheatsheet](../reference/papers/dynamic_cheatsheet_arxiv-2504.07952.md) | [CLAUDE.md / auto memory](../reference/cases/claude-code-memory_anthropic-docs.md), [Cursor Rules](../reference/cases/cursor-rules_cursor-docs.md), [AGENTS.md](../reference/cases/agents-md_agents-md-site.md), [Letta MemFS skills](../reference/cases/letta-memfs_letta-docs.md) |
| 작업 중 상태 (working) | [MemGPT](../reference/papers/memgpt_arxiv-2310.08560.md), [MEM1](../reference/papers/mem1_arxiv-2506.15841.md), [MemAgent](../reference/papers/memagent_arxiv-2507.02259.md) | [Manus todo.md·파일시스템](../reference/cases/manus-context-engineering_manus-blog.md), [Claude memory tool](../reference/cases/claude-memory-tool_anthropic-docs.md), [Anthropic 멀티에이전트 리서치](../reference/cases/multi-agent-research_anthropic-engineering.md) |
| 코드베이스 사실 | — | [GitHub Copilot Memory](../reference/cases/copilot-agentic-memory_github-blog.md) (file:line 인용 포함) |

- 2025년 이후 논문은 "사용자를 기억"보다 "경험에서 전략을 추출"(experiential) 쪽으로 이동. 최신 서베이 2편이 이 흐름을 명시한다: [Storage→Reflection→Experience](../reference/papers/survey_storage_to_experience_arxiv-2605.06716.md), [Second Half](../reference/papers/survey_agent_memory_second_half_arxiv-2602.06052.md) ("memory is increasingly the substrate through which agents self-evolve").
- 코딩 에이전트는 사람이 쓴 지시(CLAUDE.md, rules, AGENTS.md)와 에이전트가 쓴 메모리를 분리해 둔다. Claude Code auto memory는 "Claude skips anything it can derive from the codebase" ([Claude Code docs](../reference/cases/claude-code-memory_anthropic-docs.md)).

### 3.2 어떤 형태로 저장하나

| 형태 | 논문 | 실서비스 |
|---|---|---|
| 평문 파일·마크다운 | [Dynamic Cheatsheet](../reference/papers/dynamic_cheatsheet_arxiv-2504.07952.md), [ACE](../reference/papers/ace_arxiv-2510.04618.md) ("evolving playbooks") | Claude Code, [Claude memory tool](../reference/cases/claude-memory-tool_anthropic-docs.md), [Letta MemFS](../reference/cases/letta-memfs_letta-docs.md) (git), Manus, Codex/AGENTS.md, Cursor, Windsurf |
| 벡터 (+키워드) | [Think-in-Memory](../reference/papers/think_in_memory_arxiv-2311.08719.md) (LSH), [A-MEM](../reference/papers/a_mem_arxiv-2502.12110.md) (노트+링크) | [Mem0](../reference/cases/mem0_github-readme.md) (semantic+BM25+entity), [CrewAI](../reference/cases/crewai-memory_crewai-docs.md) (LanceDB), [LangGraph store](../reference/cases/langgraph-memory_langchain-docs.md), [AutoGen](../reference/cases/autogen-memory_microsoft-docs.md) |
| 지식 그래프 | [HippoRAG](../reference/papers/hipporag_arxiv-2405.14831.md), [HippoRAG 2](../reference/papers/hipporag2_arxiv-2502.14802.md), [Zep](../reference/papers/zep_arxiv-2501.13956.md), [G-Memory](../reference/papers/g_memory_arxiv-2506.07398.md), [RET-LLM](../reference/papers/ret_llm_arxiv-2305.14322.md) (triplet) | [Graphiti](../reference/cases/graphiti_github-readme.md) (bi-temporal), [cognee](../reference/cases/cognee_github-readme.md), [MemOS](../reference/cases/memos_github-readme.md) |
| 정형 DB·프로필 | [ChatDB](../reference/papers/chatdb_arxiv-2306.03901.md) (SQL) | [Memobase](../reference/cases/memobase_github-readme.md) (topic/sub_topic 프로필), [LlamaIndex](../reference/cases/llamaindex-memory_llamaindex-docs.md) (SQLite) |
| 계층형 (OS 비유) | [MemGPT](../reference/papers/memgpt_arxiv-2310.08560.md), [MemoryOS](../reference/papers/memoryos_arxiv-2506.06326.md), [MemOS](../reference/papers/memos_arxiv-2507.03724.md), [MIRIX](../reference/papers/mirix_arxiv-2507.07957.md) (6종), [LightMem](../reference/papers/lightmem_arxiv-2510.18866.md) | [Letta](../reference/cases/letta-memory_letta-docs.md) (`system/` 상시 + 나머지 필요시) |
| 파라미터·latent | [LongMem](../reference/papers/longmem_arxiv-2306.07174.md), [MemoryLLM](../reference/papers/memoryllm_arxiv-2402.04624.md), [M+](../reference/papers/mplus_arxiv-2502.00592.md), [Titans](../reference/papers/titans_arxiv-2501.00663.md), [MemoRAG](../reference/papers/memorag_arxiv-2409.05591.md) (KV 압축) | 수집 자료 중 없음 |

- 실서비스에 파라미터형 메모리는 없다. LangChain: "we don't see many (any?) agentic systems that update the weights of their LLM automatically" ([LangChain blog](../reference/cases/memory-for-agents_langchain-blog.md), 2024-10).
- 파일 기반은 벡터 인덱스를 일부러 빼는 경우가 있다: "MemFS does not include a semantic or vector index by default" ([Letta MemFS](../reference/cases/letta-memfs_letta-docs.md)).

### 3.3 누가·언제 쓰나 (write path)

| 방식 | 예 | 근거 |
|---|---|---|
| 사용자 명시 ("기억해") | ChatGPT, Gemini, M365, Claude Code, Windsurf | M365: "Copilot only saves information when there's a clear intent to remember" ([출처](../reference/cases/m365-copilot-memory_microsoft-techcommunity.md)) |
| 대화 루프 안에서 에이전트가 도구 호출 (hot path) | [MemGPT](../reference/papers/memgpt_arxiv-2310.08560.md), [Claude memory tool](../reference/cases/claude-memory-tool_anthropic-docs.md), [Copilot `store_memory`](../reference/cases/copilot-agentic-memory_github-blog.md), [LangMem](../reference/cases/langmem_github-readme.md) | LangMem: "The agent gets to decide what and when to store." |
| 턴/태스크 후 자동 추출 | [Mem0](../reference/cases/mem0_github-readme.md), [CrewAI](../reference/cases/crewai-memory_crewai-docs.md), [MemOS 플러그인](../reference/cases/memos_github-readme.md) | CrewAI: 태스크 후 사실 추출·저장, 태스크 전 회상·주입 |
| 백그라운드·오프라인 정리 | [Letta sleep-time](../reference/cases/letta-sleep-time-compute_letta-blog.md), [Letta dreaming](../reference/cases/letta-memory_letta-docs.md), [Memobase](../reference/cases/memobase_github-readme.md), [LightMem](../reference/papers/lightmem_arxiv-2510.18866.md) | Memobase: "we don't memoize users in hot path" (버퍼 1024 토큰 또는 1시간 유휴 시 처리) |
| 강화학습으로 학습된 정책 | [Memory-R1](../reference/papers/memory_r1_arxiv-2508.19828.md), [Mem-α](../reference/papers/mem_alpha_arxiv-2509.25911.md), [MEM1](../reference/papers/mem1_arxiv-2506.15841.md), [MemAgent](../reference/papers/memagent_arxiv-2507.02259.md), [Memory-T1](../reference/papers/memory_t1_arxiv-2512.20092.md), [MemRL](../reference/papers/memrl_arxiv-2601.03192.md) | Memory-R1: ADD/UPDATE/DELETE/NOOP 를 PPO·GRPO로 학습, "152 training QA pairs" |

- hot path vs 백그라운드 트레이드오프: hot path는 투명성(사용자에게 알림 가능)과 즉시성, 백그라운드는 지연 없음과 정리 품질 ([LangGraph memory](../reference/cases/langgraph-memory_langchain-docs.md)).
- Letta는 메모리 편집 도구를 주 에이전트에서 빼고 sleep-time 에이전트에만 준다. 이유: "Memory formation in MemGPT is incremental, so memories may become messy and disorganized over time" ([Letta blog](../reference/cases/letta-sleep-time-compute_letta-blog.md)).
- 실서비스에서 RL로 학습된 메모리 정책을 쓴다는 문서는 수집 자료에 없다.

### 3.4 어떻게 불러오나 (read path)

| 방식 | 예 |
|---|---|
| 항상 전부 주입 | [AutoGen ListMemory](../reference/cases/autogen-memory_microsoft-docs.md), [Memobase `context()`](../reference/cases/memobase_github-readme.md), Codex AGENTS.md (기본 32 KiB) ([출처](../reference/cases/codex-agents-md_openai-docs.md)) |
| 작은 색인은 상시, 본문은 필요할 때 (계층 로딩) | Claude Code `MEMORY.md` "first 200 lines or 25KB" + 주제 파일 ([출처](../reference/cases/claude-code-memory_anthropic-docs.md)), Letta `system/` 상시 + 나머지는 파일 트리만 ([출처](../reference/cases/letta-memory_letta-docs.md)), Cursor 4가지 활성 모드 ([출처](../reference/cases/cursor-rules_cursor-docs.md)) |
| 유사도/하이브리드 검색 | [Mem0](../reference/cases/mem0_github-readme.md), [Graphiti](../reference/cases/graphiti_github-readme.md) (semantic+BM25+graph), [CrewAI](../reference/cases/crewai-memory_crewai-docs.md) (semantic 0.5 / recency 0.3 / importance 0.2), [HippoRAG](../reference/papers/hipporag_arxiv-2405.14831.md) (Personalized PageRank) |
| 에이전트가 필요할 때 직접 읽기 (just-in-time) | [Claude memory tool](../reference/cases/claude-memory-tool_anthropic-docs.md), [Manus](../reference/cases/manus-context-engineering_manus-blog.md), [Anthropic context engineering](../reference/cases/context-engineering_anthropic-engineering.md) |
| 최근 것 + 사용 직전 검증 | [GitHub Copilot](../reference/cases/copilot-agentic-memory_github-blog.md): 최근 메모리 주입 → 인용된 코드 위치를 현재 브랜치에서 확인 → "Only validated facts are used" ([docs](../reference/cases/copilot-memory_github-docs.md)) |

- 서베이·벤치마크의 결론도 "더 많이 넣기"가 답이 아니라는 쪽: [LongMemEval](../reference/papers/longmemeval_arxiv-2410.10813.md)은 상용 어시스턴트·장문맥 LLM이 지속 대화에서 "30% accuracy drop"을 보였다고 보고하고, 설계를 indexing / retrieval / reading 3단계로 분해한다.
- Anthropic: "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome" ([출처](../reference/cases/context-engineering_anthropic-engineering.md)).

### 3.5 갱신·충돌·망각

| 전략 | 예 | 근거 |
|---|---|---|
| 덧붙이기만 (append-only) | [Mem0 (현 README)](../reference/cases/mem0_github-readme.md) | "Single-pass ADD-only extraction -- one LLM call, no UPDATE/DELETE". 최신성은 검색 시 시간 인지 랭킹으로 처리 |
| LLM이 CRUD 결정 | [Mem0 논문](../reference/papers/mem0_arxiv-2504.19413.md) (초록 표현은 "extracting, consolidating" — 세부 연산은 본문 미확인), [CrewAI](../reference/cases/crewai-memory_crewai-docs.md) (유사도 0.85 초과 시 keep/update/delete/insert_new), [Memory-R1](../reference/papers/memory_r1_arxiv-2508.19828.md) (이 결정을 RL로 학습) | LangGraph: "some models may default to over-inserting and others may default to over-updating" |
| 지우지 않고 무효화 (bi-temporal) | [Graphiti/Zep](../reference/cases/graphiti_github-readme.md) | "old facts are invalidated — not deleted" |
| 사용 시점 검증 + 미사용 만료 | [GitHub Copilot](../reference/cases/copilot-memory_github-docs.md) | 미사용 항목 "automatically deleted after 28 days", 검증·사용 시 타이머 리셋 가능 |
| 망각 곡선 | [MemoryBank](../reference/papers/memorybank_arxiv-2305.10250.md) | Ebbinghaus 곡선 기반 경과시간·중요도로 망각/강화 |
| 오프라인 통합 | [Letta dreaming](../reference/cases/letta-memory_letta-docs.md), [LightMem](../reference/papers/lightmem_arxiv-2510.18866.md) (sleep-time update), [Generative Agents](../reference/papers/generative_agents_arxiv-2304.03442.md) (reflection) | — |
| 버전 관리 | [Letta MemFS](../reference/cases/letta-memfs_letta-docs.md) (모든 편집 git 커밋), [MemOS](../reference/papers/memos_arxiv-2507.03724.md) (MemCube에 provenance·versioning 메타데이터) | — |
| 정리 없음 / 사람·개발자 몫 | [Claude Code](../reference/cases/claude-code-memory_anthropic-docs.md) (충돌 시 "Claude may pick one arbitrarily"), [Claude memory tool](../reference/cases/claude-memory-tool_anthropic-docs.md) ("Periodically delete memory files that haven't been accessed in a long time" 권고) | — |

- 반복 갱신의 함정: [ACE](../reference/papers/ace_arxiv-2510.04618.md)는 반복 재작성이 세부를 깎아내는 "context collapse"와 요약 편향 "brevity bias"를 지적하고, 전체 재작성 대신 구조화된 증분 갱신을 쓴다. [Manus](../reference/cases/manus-context-engineering_manus-blog.md)도 "any irreversible compression carries risk"라며 복원 가능한 압축(URL·경로 보존)만 쓴다.
- GitHub는 오프라인 큐레이션(중복 제거·충돌 해결)을 비용 때문에 명시적으로 기각하고 읽을 때 검증으로 대체했다: "Information retrieval is an asymmetrical problem: It's hard to solve, but easy to verify" ([출처](../reference/cases/copilot-agentic-memory_github-blog.md)).

### 3.6 범위·사용자 통제

- 범위를 좁히는 것이 기본: 프로젝트별 (Claude 앱 "a separate memory for each project", [출처](../reference/cases/claude-memory_anthropic-news.md)), 저장소별 (Claude Code, Copilot), 워크스페이스별 (Windsurf "Memories generated in one workspace will not be available in another", [출처](../reference/cases/windsurf-memories_devin-docs.md)). Anthropic은 프로젝트 분리를 "a safety guardrail"로 설명.
- 권한과 연동: Copilot 저장소 메모리는 쓰기 권한자 활동에서만 생성, 읽기 권한자는 사용만 ([출처](../reference/cases/copilot-memory_github-docs.md)).
- 상용 어시스턴트 공통 통제: 보기·수정·삭제, 전체 끄기, 메모리 없는 모드 (ChatGPT Temporary chat, Claude Incognito, Gemini Temporary Chat — 최대 72시간 보관, [출처](../reference/cases/gemini-personal-context_google-blog.md)), 저장 알림 ("Memory updated").
- 기본값은 갈린다: Gemini 과거 대화 참조 "on by default", Claude 앱 "fully optional", Copilot은 개인 요금제 기본 켜짐·엔터프라이즈는 관리자 활성화 필요.
- 삭제는 연쇄되지 않는다: "Deleting a chat doesn't erase its memories; you must delete the memory itself" ([ChatGPT blog](../reference/cases/chatgpt-memory_openai-blog.md)). 삭제된 저장 메모리 로그는 최대 30일 보관 가능 ([FAQ](../reference/cases/chatgpt-memory_openai-help-faq.md)).
- 다중 사용자·다중 에이전트 공유: [CrewAI](../reference/cases/crewai-memory_crewai-docs.md) private scope·slice, [MemOS](../reference/cases/memos_github-readme.md) cube, [G-Memory](../reference/papers/g_memory_arxiv-2506.07398.md). Graphiti 참조 서버는 "no authentication, no authorization, and no prompt-injection protection"이라고 스스로 밝힘 ([출처](../reference/cases/graphiti_github-readme.md)).

### 3.7 보고된 수치 (출처별 자체 평가)

| 시스템 | 수치 | 비교 대상·조건 | 성격 |
|---|---|---|---|
| [Mem0 논문](../reference/papers/mem0_arxiv-2504.19413.md) | LLM-as-a-Judge 26% 상대 개선, p95 지연 91%↓, 토큰 90%↑ 절감 | LoCoMo, OpenAI 메모리 대비 / full-context 대비 | 자사 논문 |
| [Mem0 README](../reference/cases/mem0_github-readme.md) | LoCoMo 92.5, LongMemEval 94.4 | 관리형 플랫폼 기준, "proprietary optimizations not available in the open-source SDK" | 자사 |
| [MemOS README](../reference/cases/memos_github-readme.md) | LoCoMo 88.83, LongMemEval 89.20 | 자사 벤치마크 포함 | 자사 |
| [Zep 논문](../reference/papers/zep_arxiv-2501.13956.md) | DMR 94.8% vs MemGPT 93.4%, LongMemEval 최대 18.5% 개선, 지연 90%↓ | 베이스라인 구현 대비 | 자사 논문 |
| [MIRIX](../reference/papers/mirix_arxiv-2507.07957.md) | LoCoMo 85.4% | — | 저자 논문 |
| [MemoryOS](../reference/papers/memoryos_arxiv-2506.06326.md) | LoCoMo F1 49.11% 평균 개선 | GPT-4o-mini 베이스라인 대비 | 저자 논문 |
| [LightMem](../reference/papers/lightmem_arxiv-2510.18866.md) | QA 최대 7.7% / 29.3%↑, 토큰 최대 38x / 20.9x↓ | LongMemEval / LoCoMo | 저자 논문 |
| [Claude memory tool + context editing](../reference/cases/claude-context-management_anthropic-news.md) | 39% 개선 (context editing 단독 29%), 100턴 웹검색에서 토큰 84%↓ | Anthropic 내부 평가 | 자사 |
| [GitHub Copilot Memory](../reference/cases/copilot-agentic-memory_github-blog.md) | PR 머지율 90% vs 83%, 리뷰 정밀도 +3% / 재현율 +4%, p < 0.00001 | 실사용 A/B 테스트 | 자사, 방법 설명 가장 상세 |
| [AWM](../reference/papers/agent_workflow_memory_arxiv-2409.07429.md) | Mind2Web 24.6%, WebArena 51.1% 상대 성공률↑ | 웹 내비게이션 | 저자 논문 |
| [Dynamic Cheatsheet](../reference/papers/dynamic_cheatsheet_arxiv-2504.07952.md) | GPT-4o Game of 24: 10% → 99% | 정답 라벨 없이 테스트 시 학습 | 저자 논문 |
| [ACE](../reference/papers/ace_arxiv-2510.04618.md) | 에이전트 +10.6%, 금융 +8.6% | AppWorld 등 | 저자 논문 |

- 같은 LoCoMo에서 Mem0 92.5 / MemOS 88.83 / MIRIX 85.4 / Supermemory "#1 on every major AI memory benchmark" ([출처](../reference/cases/supermemory_github-readme.md))가 동시에 주장된다. 평가 설정(판정 모델, 지표, 버전)이 달라 **직접 비교 불가**.
- 독립 비교 벤치마크의 결론은 반대로 신중하다: [MemoryAgentBench](../reference/papers/memoryagentbench_arxiv-2507.05257.md)는 정확한 검색·테스트 시 학습·장거리 이해·선택적 망각 4개 역량 중 "current methods fall short of mastering all four", [LoCoMo](../reference/papers/locomo_arxiv-2402.17753.md)는 장문맥·RAG 모두 "substantially lag behind human performance".

## 4. 해석

1. **연구와 실서비스가 다른 문제를 풀고 있다.**
   - 논문은 저장 구조(그래프·계층·latent)와 학습된 관리 정책(RL)에 집중한다.
   - 실서비스, 특히 코딩 에이전트는 마크다운 파일 + 작은 색인 상시 로딩 + 나머지 필요시 읽기로 수렴했다 (Claude Code, Letta MemFS, Codex, Cursor, Windsurf, Manus).
   - 이유로 문서들이 드는 것: 사람이 읽고 고칠 수 있음, git으로 버전 관리, 모델이 이미 파일 도구를 잘 씀.
2. **실서비스의 핵심 난제는 "찾기"보다 "아직 맞는가"다.**
   - GitHub: "The core challenge for memory systems isn't about information retrieval, but ensuring that any stored knowledge remains valid as code evolves" ([출처](../reference/cases/copilot-agentic-memory_github-blog.md)).
   - 대응이 셋으로 갈린다: 읽을 때 검증(Copilot), 지우지 않고 유효기간 표시(Graphiti), 백그라운드 재정리(Letta). 무엇이 나은지 비교한 자료는 수집 범위에 없다.
3. **갱신 연산은 아직 합의가 없다.**
   - Mem0는 논문(2025-04)에서 LLM이 추출·통합하던 방식에서 현 README의 ADD-only로 바뀌었다. 위 LangGraph 지적("over-inserting / over-updating")과 ACE의 context collapse가 같은 문제의 다른 면으로 보인다 (추정).
   - RL 논문들(Memory-R1, Mem-α)은 바로 이 결정을 학습 대상으로 삼는다.
4. **메모리의 중심이 "사용자 사실"에서 "경험·절차"로 옮겨 가는 중.**
   - 2024-09 AWM 이후 Memp, ReasoningBank, ACE, Dynamic Cheatsheet, MemRL 모두 가중치를 바꾸지 않고 전략·워크플로우를 쌓아 성능을 올린다.
   - 실서비스에서 같은 위치를 차지하는 것이 CLAUDE.md·rules·skills다. 차이는 실서비스는 대부분 사람이 쓰거나 사람이 검토한다는 점.
5. **벤치마크 수치는 설계 판단 근거로 약하다.**
   - LoCoMo·LongMemEval 점수가 벤더마다 자체 측정이고 서로 다른 설정이다.
   - 실제 효과 근거로는 GitHub의 A/B 테스트가 가장 구체적이지만 효과 크기는 작다 (머지율 +7%p).

## 5. 남은 질문

- 논문 본문 미확인: 위 아키텍처 비교는 초록 수준. Mem0·Zep·A-MEM·MemGPT·LongMemEval은 본문(특히 실험 설정)을 읽어야 수치 비교가 가능.
- ChatGPT·Gemini·Claude 앱의 저장·검색 내부 구조는 공개 문서에 없음. ChatGPT가 `save_memories` 도구로 upsert한다는 것은 LangGraph 문서의 2차 언급뿐 ([출처](../reference/cases/langgraph-memory_langchain-docs.md)).
- 갱신 전략(append-only / LLM CRUD / 무효화 / 읽기 시 검증)을 같은 조건에서 비교한 자료 없음 → 직접 실험 후보.
- 파일 기반 메모리가 수천 항목 이상으로 커질 때의 한계 (색인 200줄 제한 이후) 관련 자료 없음.
- 2026-06 이후 쏟아진 메모리 벤치마크(약 25편)는 영향력 판단이 어려워 수집에서 제외. 필요하면 추가 조사.
- 메모리 오염·프롬프트 인젝션 같은 보안 측면은 사례 문서에 단편적으로만 있음 (Graphiti 경고, Copilot 적대적 메모리 테스트).

## 출처

출처마다 로컬 원문 파일과 원 URL을 같이 둔다.

### 논문 (arXiv)

- MemGPT — [원문](../reference/papers/memgpt_arxiv-2310.08560.md) · https://arxiv.org/abs/2310.08560
- Generative Agents — [원문](../reference/papers/generative_agents_arxiv-2304.03442.md) · https://arxiv.org/abs/2304.03442
- Reflexion — [원문](../reference/papers/reflexion_arxiv-2303.11366.md) · https://arxiv.org/abs/2303.11366
- CoALA — [원문](../reference/papers/coala_arxiv-2309.02427.md) · https://arxiv.org/abs/2309.02427
- MemoryBank — [원문](../reference/papers/memorybank_arxiv-2305.10250.md) · https://arxiv.org/abs/2305.10250
- RET-LLM — [원문](../reference/papers/ret_llm_arxiv-2305.14322.md) · https://arxiv.org/abs/2305.14322
- Voyager — [원문](../reference/papers/voyager_arxiv-2305.16291.md) · https://arxiv.org/abs/2305.16291
- ChatDB — [원문](../reference/papers/chatdb_arxiv-2306.03901.md) · https://arxiv.org/abs/2306.03901
- LongMem — [원문](../reference/papers/longmem_arxiv-2306.07174.md) · https://arxiv.org/abs/2306.07174
- Think-in-Memory — [원문](../reference/papers/think_in_memory_arxiv-2311.08719.md) · https://arxiv.org/abs/2311.08719
- MemoryLLM — [원문](../reference/papers/memoryllm_arxiv-2402.04624.md) · https://arxiv.org/abs/2402.04624
- HippoRAG — [원문](../reference/papers/hipporag_arxiv-2405.14831.md) · https://arxiv.org/abs/2405.14831
- MemoRAG — [원문](../reference/papers/memorag_arxiv-2409.05591.md) · https://arxiv.org/abs/2409.05591
- Agent Workflow Memory — [원문](../reference/papers/agent_workflow_memory_arxiv-2409.07429.md) · https://arxiv.org/abs/2409.07429
- Titans — [원문](../reference/papers/titans_arxiv-2501.00663.md) · https://arxiv.org/abs/2501.00663
- Zep — [원문](../reference/papers/zep_arxiv-2501.13956.md) · https://arxiv.org/abs/2501.13956
- M+ — [원문](../reference/papers/mplus_arxiv-2502.00592.md) · https://arxiv.org/abs/2502.00592
- A-MEM — [원문](../reference/papers/a_mem_arxiv-2502.12110.md) · https://arxiv.org/abs/2502.12110
- HippoRAG 2 — [원문](../reference/papers/hipporag2_arxiv-2502.14802.md) · https://arxiv.org/abs/2502.14802
- Mem0 — [원문](../reference/papers/mem0_arxiv-2504.19413.md) · https://arxiv.org/abs/2504.19413
- MemoryOS — [원문](../reference/papers/memoryos_arxiv-2506.06326.md) · https://arxiv.org/abs/2506.06326
- G-Memory — [원문](../reference/papers/g_memory_arxiv-2506.07398.md) · https://arxiv.org/abs/2506.07398
- MemOS — [원문](../reference/papers/memos_arxiv-2507.03724.md) · https://arxiv.org/abs/2507.03724
- MIRIX — [원문](../reference/papers/mirix_arxiv-2507.07957.md) · https://arxiv.org/abs/2507.07957
- Memp — [원문](../reference/papers/memp_arxiv-2508.06433.md) · https://arxiv.org/abs/2508.06433
- LightMem — [원문](../reference/papers/lightmem_arxiv-2510.18866.md) · https://arxiv.org/abs/2510.18866
- Dynamic Cheatsheet — [원문](../reference/papers/dynamic_cheatsheet_arxiv-2504.07952.md) · https://arxiv.org/abs/2504.07952
- MEM1 — [원문](../reference/papers/mem1_arxiv-2506.15841.md) · https://arxiv.org/abs/2506.15841
- MemAgent — [원문](../reference/papers/memagent_arxiv-2507.02259.md) · https://arxiv.org/abs/2507.02259
- Memory-R1 — [원문](../reference/papers/memory_r1_arxiv-2508.19828.md) · https://arxiv.org/abs/2508.19828
- ReasoningBank — [원문](../reference/papers/reasoningbank_arxiv-2509.25140.md) · https://arxiv.org/abs/2509.25140
- Mem-α — [원문](../reference/papers/mem_alpha_arxiv-2509.25911.md) · https://arxiv.org/abs/2509.25911
- ACE — [원문](../reference/papers/ace_arxiv-2510.04618.md) · https://arxiv.org/abs/2510.04618
- Memory-T1 — [원문](../reference/papers/memory_t1_arxiv-2512.20092.md) · https://arxiv.org/abs/2512.20092
- MemRL — [원문](../reference/papers/memrl_arxiv-2601.03192.md) · https://arxiv.org/abs/2601.03192
- Survey: Rethinking Memory — [원문](../reference/papers/survey_rethinking_memory_arxiv-2505.00675.md) · https://arxiv.org/abs/2505.00675
- Survey: Memory in the Age of AI Agents — [원문](../reference/papers/survey_memory_age_of_agents_arxiv-2512.13564.md) · https://arxiv.org/abs/2512.13564
- Survey: Agent Memory in the Second Half — [원문](../reference/papers/survey_agent_memory_second_half_arxiv-2602.06052.md) · https://arxiv.org/abs/2602.06052
- Survey: From Storage to Experience — [원문](../reference/papers/survey_storage_to_experience_arxiv-2605.06716.md) · https://arxiv.org/abs/2605.06716
- LoCoMo — [원문](../reference/papers/locomo_arxiv-2402.17753.md) · https://arxiv.org/abs/2402.17753
- LongMemEval — [원문](../reference/papers/longmemeval_arxiv-2410.10813.md) · https://arxiv.org/abs/2410.10813
- MemoryAgentBench — [원문](../reference/papers/memoryagentbench_arxiv-2507.05257.md) · https://arxiv.org/abs/2507.05257

### 구축 사례

- ChatGPT Memory (OpenAI blog) — [원문](../reference/cases/chatgpt-memory_openai-blog.md) · https://openai.com/index/memory-and-new-controls-for-chatgpt/
- ChatGPT Memory FAQ — [원문](../reference/cases/chatgpt-memory_openai-help-faq.md) · https://help.openai.com/en/articles/8590148-memory-faq
- Claude memory (Anthropic) — [원문](../reference/cases/claude-memory_anthropic-news.md) · https://www.anthropic.com/news/memory
- Claude context management — [원문](../reference/cases/claude-context-management_anthropic-news.md) · https://www.anthropic.com/news/context-management
- Claude memory tool docs — [원문](../reference/cases/claude-memory-tool_anthropic-docs.md) · https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- Gemini personal context — [원문](../reference/cases/gemini-personal-context_google-blog.md) · https://blog.google/products/gemini/temporary-chats-privacy-controls/
- Gemini saved info — [원문](../reference/cases/gemini-memory_google-help.md) · https://support.google.com/gemini/answer/16413516
- Microsoft 365 Copilot Memory — [원문](../reference/cases/m365-copilot-memory_microsoft-techcommunity.md) · https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-copilot-memory-a-more-productive-and-personalized-ai-for-the-way-you-work/4432059
- Claude Code memory — [원문](../reference/cases/claude-code-memory_anthropic-docs.md) · https://code.claude.com/docs/en/memory
- Cursor Rules — [원문](../reference/cases/cursor-rules_cursor-docs.md) · https://cursor.com/docs/context/rules
- Windsurf Cascade Memories — [원문](../reference/cases/windsurf-memories_devin-docs.md) · https://docs.devin.ai/windsurf/plugins/cascade/memories
- GitHub Copilot agentic memory (blog) — [원문](../reference/cases/copilot-agentic-memory_github-blog.md) · https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/
- GitHub Copilot Memory (docs) — [원문](../reference/cases/copilot-memory_github-docs.md) · https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-memory
- AGENTS.md — [원문](../reference/cases/agents-md_agents-md-site.md) · https://agents.md/
- Codex AGENTS.md — [원문](../reference/cases/codex-agents-md_openai-docs.md) · https://developers.openai.com/codex/guides/agents-md
- Letta Memory — [원문](../reference/cases/letta-memory_letta-docs.md) · https://docs.letta.com/agent-sdk/memory/
- Letta MemFS — [원문](../reference/cases/letta-memfs_letta-docs.md) · https://docs.letta.com/concepts/memfs/
- Letta Sleep-time Compute — [원문](../reference/cases/letta-sleep-time-compute_letta-blog.md) · https://www.letta.com/blog/sleep-time-compute
- Mem0 README — [원문](../reference/cases/mem0_github-readme.md) · https://github.com/mem0ai/mem0
- Graphiti README — [원문](../reference/cases/graphiti_github-readme.md) · https://github.com/getzep/graphiti
- LangMem README — [원문](../reference/cases/langmem_github-readme.md) · https://github.com/langchain-ai/langmem
- LangGraph memory — [원문](../reference/cases/langgraph-memory_langchain-docs.md) · https://docs.langchain.com/oss/python/concepts/memory
- LlamaIndex memory — [원문](../reference/cases/llamaindex-memory_llamaindex-docs.md) · https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/memory/
- cognee README — [원문](../reference/cases/cognee_github-readme.md) · https://github.com/topoteretes/cognee
- Memobase README — [원문](../reference/cases/memobase_github-readme.md) · https://github.com/memodb-io/memobase
- MemOS README — [원문](../reference/cases/memos_github-readme.md) · https://github.com/MemTensor/MemOS
- Supermemory README — [원문](../reference/cases/supermemory_github-readme.md) · https://github.com/supermemoryai/supermemory
- CrewAI memory — [원문](../reference/cases/crewai-memory_crewai-docs.md) · https://docs.crewai.com/en/concepts/memory
- AutoGen memory — [원문](../reference/cases/autogen-memory_microsoft-docs.md) · https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html
- Memory for agents (LangChain) — [원문](../reference/cases/memory-for-agents_langchain-blog.md) · https://blog.langchain.com/memory-for-agents/
- Manus context engineering — [원문](../reference/cases/manus-context-engineering_manus-blog.md) · https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- Effective context engineering (Anthropic) — [원문](../reference/cases/context-engineering_anthropic-engineering.md) · https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Multi-agent research system (Anthropic) — [원문](../reference/cases/multi-agent-research_anthropic-engineering.md) · https://www.anthropic.com/engineering/multi-agent-research-system

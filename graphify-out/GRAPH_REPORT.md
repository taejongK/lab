# Graph Report - npc-engine  (2026-11-22)

## Corpus Check
- 110 files · ~139,824 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 22 file(s) not represented in the graph (top: (none) 20, .graphify-bak 1, .lock 1)

## Summary
- 1023 nodes · 1139 edges · 82 communities (74 shown, 8 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f5d52a1e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- new-study Skill
- Laya
- Memory tool
- 01.jev/docs/notes/02.오픈소스-복제-모델.md
- main.py
- Calibration
- 01.jev/CLAUDE.md
- {기능명} — 로직 인계 문서
- 자동 문서화 규칙 (필수)
- 02.llm_world
- {디렉터리 경로 또는 패키지명}
- {기능명} — 개발 로그
- For AI Agents
- .say
- LLM World
- Handover Index
- frontend/README.md
- server/README.md
- server
- World
- 공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사
- Memory
- 2026-10-13
- 01. 아키텍처 (MVP 초안)
- 02.llm_world/docs/reference/README.md
- docs
- {기능명} — 로직 인계 문서
- CLAUDE.md files
- 자동 문서화 규칙 (필수)
- Jev
- getzep/graphiti README (Zep 시간 지식그래프)
- 03.image_filter
- {디렉터리 경로 또는 패키지명}
- LLM logit readout approach
- DecisionModel.forward
- {기능명} — 개발 로그
- 01. 에이전트 메모리 주요 아키텍처 패턴 (2025~2026)
- Reference
- chatgpt-memory_openai-help-faq.md
- cases/README.md
- image_filter
- 2026_10_19.md
- Build with Supermemory (API)
- memodb-io/memobase README
- Rules
- FAQ
- topoteretes/cognee README
- 05.agent_memory/docs/index.md
- Memory
- MemTensor/MemOS README
- Long-term memory
- 🚀 Quickstart Guide <a name="quickstart"></a>
- Action-Based Conversations Dataset (ABCD)
- 자동 문서화 규칙 (필수)
- Effective context engineering for AI agents
- About Copilot Memory
- How we built our multi-agent research system
- Cascade Memories (Windsurf)
- 05.agent_memory
- autogen-memory_microsoft-docs.md
- Memory for agents
- For AI Agents
- Custom instructions with AGENTS.md (Codex)
- Sleep-time Compute
- Introducing Copilot Memory: A More Productive and Personalized AI for the Way You Work
- Context Engineering for AI Agents: Lessons from Building Manus
- Managing context on the Claude Developer Platform
- Bringing memory to Claude
- Save info & preferences
- MemFS | Letta Docs (git-versioned memory filesystem)
- Gemini adds Temporary Chats and new personalization features
- Memory | Letta Docs (memory blocks, MemFS, dreaming)
- Cases — 실제 에이전트 메모리 구현 사례 원문
- chatgpt-memory_openai-blog.md
- LangMem
- letta_github-readme.md
- 2026_10_28
- 2026_11_01
- 2026_11_04
- mem0_github-readme.md
- 2026-10-27
- 05.agent_memory/README.md

## God Nodes (most connected - your core abstractions)
1. `Memory` - 21 edges
2. `getzep/graphiti README (Zep 시간 지식그래프)` - 19 edges
3. `Memory tool` - 14 edges
4. `memodb-io/memobase README` - 14 edges
5. `Jev` - 14 edges
6. `topoteretes/cognee README` - 13 edges
7. `2026-10-13` - 12 edges
8. `decide()` - 11 edges
9. `Rules` - 11 edges
10. `World` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Study README Template` --semantically_similar_to--> `Project README Template (status/period/what-why/results/conclusion)`  [INFERRED] [semantically similar]
  .claude/skills/new-study/template/README.md → README.md
- `MVP 5단계: LLM 판단 + 고착 문제 3인 논의` --references--> `decide()`  [INFERRED]
  02.llm_world/docs/worklog/2026_10_13.md → 02.llm_world/server/main.py
- `결정 사항` --references--> `npc_loop()`  [INFERRED]
  02.llm_world/docs/plan/active/20261013_mvp_devlog.md → 02.llm_world/server/main.py
- `Key Files` --references--> `World`  [INFERRED]
  02.llm_world/server/AGENTS.md → 02.llm_world/server/main.py
- `Key Files` --references--> `decide()`  [INFERRED]
  02.llm_world/server/AGENTS.md → 02.llm_world/server/main.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Three implementation lineages of Jev replicas** — 01_jev_docs_notes_02_오픈소스_복제_모델_llm_logit_readout, 01_jev_docs_notes_02_오픈소스_복제_모델_llm_decision_head, 01_jev_docs_notes_02_오픈소스_복제_모델_encoder_head, 01_jev_docs_notes_01_jev_소개와_개념_jev [EXTRACTED 1.00]
- **Jev typed question primitives (Noul/Choice/Score)** — 01_jev_docs_notes_01_jev_소개와_개념_noul, 01_jev_docs_notes_01_jev_소개와_개념_choice, 01_jev_docs_notes_01_jev_소개와_개념_score, 01_jev_docs_notes_03_laya_모델_구조_k_way_reduction [EXTRACTED 1.00]
- **new-study Scaffold Output Files** — _claude_skills_new_study_skill_new_study, _claude_skills_new_study_template_readme_study_readme, _claude_skills_new_study_template_agents_study_agents_md, _claude_skills_new_study_template_claude_auto_doc_rules, _claude_skills_new_study_template_docs_reference_readme_reference_index, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **worklog-discipline Feature Documentation Lifecycle (devlog -> handover -> index)** — _claude_skills_new_study_template_claude_devlog_rule, _claude_skills_new_study_template_claude_handover_rule, _claude_skills_new_study_template_docs_plan_templates_dev_log_template_dev_log_template, _claude_skills_new_study_template_docs_plan_templates_handover_template_handover_template, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **Experiment Isolation Principle** — claude_independent_experiment_folders, readme_self_contained_projects, claude_pep723_uv_run, readme_shared_promotion_rule [INFERRED 0.75]
- **Laya calibration pipeline (RLCD loss, proper scoring, bucket temperature)** — 01_jev_docs_notes_03_laya_모델_구조_rlcd_loss, 01_jev_docs_notes_03_laya_모델_구조_proper_reward, 01_jev_docs_notes_03_laya_모델_구조_temp_bucket, 01_jev_docs_notes_03_laya_모델_구조_answer_confidence, 01_jev_docs_notes_01_jev_소개와_개념_calibration [INFERRED 0.85]

## Communities (82 total, 8 thin omitted)

### Community 0 - "new-study Skill"
Cohesion: 0.10
Nodes (17): new-study Skill, Study Folder Structure (docs/notes, reference, worklog, plan), Study AGENTS.md Template, worklog-discipline Plugin (/init-workstructure), Handover Index, AGENTS_TEMPLATE, DEV_LOG_TEMPLATE, HANDOVER_TEMPLATE (+9 more)

### Community 1 - "Laya"
Cohesion: 0.19
Nodes (15): RLCD (Reinforcement Learning for Calibrated Decisions), decider, Decision Index, Dohnuts, Encoder + head approach, kev, Laya, LLM backbone + trained decision head approach (+7 more)

### Community 2 - "Memory tool"
Cohesion: 0.05
Nodes (43): Basic usage, Context editing integration, create, delete, Directory handling, Directory handling, Directory handling, Directory handling (+35 more)

### Community 3 - "01.jev/docs/notes/02.오픈소스-복제-모델.md"
Cohesion: 0.31
Nodes (4): awesome-jev, Four-layer license check (code/weights/base/data), new-study skill, Legacy Sept research (git 932e704 2026-09-jev/)

### Community 4 - "main.py"
Cohesion: 0.06
Nodes (14): MVP 4단계: NPC 랜덤 목적지 이동, ask(), load(), decide(), lifespan(), nearest_place(), npc_loop(), observe() (+6 more)

### Community 5 - "Calibration"
Cohesion: 0.22
Nodes (8): Confidence-threshold routing (auto / human review / reasoning LLM), ECE (Expected Calibration Error), Post-hoc temperature scaling, Act head (act/escalate), answer_confidence vs normalized-entropy confidence, _decode_answers, Guo et al. 2017 (On Calibration of Modern Neural Networks), Per-bucket temperature (temp_bucket)

### Community 7 - "{기능명} — 로직 인계 문서"
Cohesion: 0.14
Nodes (13): 1단계: {단계명}, 2단계: {단계명}, 개요, 구현 시 주의사항, {기능명} — 로직 인계 문서, 단계별 로직 상세, 데이터 흐름, 설계 결정 사항 (+5 more)

### Community 8 - "자동 문서화 규칙 (필수)"
Cohesion: 0.17
Nodes (10): 개발 규칙, 개발 중 방향/결정 변경 시 (devlog 갱신), 기능 개발 시작 시 (devlog), 기능 구현 완료 시 (인계 문서), 디렉터리 구조 변경 시 (AGENTS.md 계층), 문서 위치, 인계 완료 시, 자동 문서화 규칙 (필수) (+2 more)

### Community 9 - "02.llm_world"
Cohesion: 0.22
Nodes (8): 02.llm_world, Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory

### Community 10 - "{디렉터리 경로 또는 패키지명}"
Cohesion: 0.22
Nodes (8): Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory, {디렉터리 경로 또는 패키지명}

### Community 11 - "{기능명} — 개발 로그"
Cohesion: 0.25
Nodes (7): 개발 계획, 결정 사항, {기능명} — 개발 로그, 메모, 목표, 변경 이력, 현재 상태

### Community 12 - "For AI Agents"
Cohesion: 0.25
Nodes (7): Common Patterns, For AI Agents, frontend, Key Files, Purpose, Testing Requirements, Working In This Directory

### Community 13 - ".say"
Cohesion: 0.20
Nodes (9): 프로토콜, MVP — 개발 로그, 개발 계획, 결정 사항, 메모, 목표, 변경 이력, 현재 상태 (+1 more)

### Community 14 - "LLM World"
Cohesion: 0.20
Nodes (7): LLM World, 구성, 목표, 문서, 범위 밖 (지금은), 스택, 완료 기준 (MVP)

### Community 15 - "Handover Index"
Cohesion: 0.50
Nodes (3): Handover Index, 인계 대기 중, 인계 현황

### Community 19 - "World"
Cohesion: 0.24
Nodes (5): MVP 2단계: 서버 뼈대, MVP 3단계: 프론트 뼈대, bfs(), walkable(), World

### Community 20 - "공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사"
Cohesion: 0.07
Nodes (26): docs, notes, plan, reference, report, worklog, Handover Index, 인계 대기 중 (+18 more)

### Community 21 - "Memory"
Cohesion: 0.04
Nodes (45): Best Practices for Scope Design, Composite Scoring, Configuration Reference, Crew Shutdown, Discovery, Embedder Configuration, Failure Behavior, Four Ways to Use Memory (+37 more)

### Community 22 - "2026-10-13"
Cohesion: 0.22
Nodes (8): 02.llm_world 폴더 생성 및 목표 설정, 2026-10-13, MVP 1단계: uzu 스모크 테스트, MVP 5단계: LLM 판단 + 고착 문제 3인 논의, MVP 7단계: 도트 그래픽, 개발 전 규칙·문서 세팅, 기술 스택 결정 반영, 스택 확정: 도트 Canvas 2D, WebSocket, Qwen 3.5 0.8B

### Community 23 - "01. 아키텍처 (MVP 초안)"
Cohesion: 0.25
Nodes (7): 01. 아키텍처 (MVP 초안), NPC 판단, 미확인 / 열린 질문, 서버 루프, 월드, 전체 구조, 출처

### Community 24 - "02.llm_world/docs/reference/README.md"
Cohesion: 0.38
Nodes (5): Gneiting & Raftery 2007 (Strictly Proper Scoring Rules), proper_reward (log + spherical + RPS), Shao et al. 2024 DeepSeekMath (GRPO), Williams 1992 (REINFORCE), Reference

### Community 25 - "docs"
Cohesion: 0.40
Nodes (5): docs, notes, reference, report, worklog

### Community 27 - "{기능명} — 로직 인계 문서"
Cohesion: 0.14
Nodes (13): 1단계: {단계명}, 2단계: {단계명}, 개요, 구현 시 주의사항, {기능명} — 로직 인계 문서, 단계별 로직 상세, 데이터 흐름, 설계 결정 사항 (+5 more)

### Community 31 - "CLAUDE.md files"
Cohesion: 0.05
Nodes (42): AGENTS.md, Audit and edit your memory, Audit your instruction files, Auto memory, Choose where to put CLAUDE.md files, Choose which instruction files load, Claude ignores the end of my subdirectory CLAUDE.md, Claude isn't following my CLAUDE.md (+34 more)

### Community 32 - "자동 문서화 규칙 (필수)"
Cohesion: 0.18
Nodes (9): 디렉터리 구조 변경 시 (AGENTS.md 계층), 문서 구조 (research), 문서 위치, 문서를 만들거나 옮길 때 (docs/index.md), 실험 결과가 나오거나 보고서를 쓸 때 (docs/report), 자동 문서화 규칙 (필수), 자료를 조사했을 때 (docs/reference), 커밋 시 (docs/worklog 날짜별 로그) — 항상 (+1 more)

### Community 36 - "Jev"
Cohesion: 0.24
Nodes (8): Choice primitive (up to 255 options), Jev, Kahneman Dual-Process Theory (System 1/System 2), Noul primitive (yes/no), Score primitive (ordered scale), Jev suitability 6-question checklist, TypeSafe AI, typesafe-sdk-python

### Community 37 - "getzep/graphiti README (Zep 시간 지식그래프)"
Cohesion: 0.05
Nodes (42): Amazon Neptune, Configurable Prompts, Contributing, Database Configuration, Default to Low Concurrency; LLM Provider 429 Rate Limit Errors, Documentation, FalkorDB with Custom Database Name, getzep/graphiti README (Zep 시간 지식그래프) (+34 more)

### Community 39 - "03.image_filter"
Cohesion: 0.22
Nodes (8): 03.image_filter, Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory

### Community 40 - "{디렉터리 경로 또는 패키지명}"
Cohesion: 0.22
Nodes (8): Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory, {디렉터리 경로 또는 패키지명}

### Community 44 - "LLM logit readout approach"
Cohesion: 0.29
Nodes (7): Constrained decoding (null hypothesis), Sean Goedecke skeptical analysis, AnyJev, JevBench, Position (option-order) bias, SemIf (OpenJev), parallel_layout (order-invariant layout, undeployed)

### Community 45 - "DecisionModel.forward"
Cohesion: 0.29
Nodes (5): build_sequence / build_head, DecisionModel.forward, [MASK]-per-option scoring, ModernBERT-large encoder, Warner et al. 2024 (ModernBERT)

### Community 46 - "{기능명} — 개발 로그"
Cohesion: 0.25
Nodes (7): 개발 계획, 결정 사항, {기능명} — 개발 로그, 메모, 목표, 변경 이력, 현재 상태

### Community 48 - "01. 에이전트 메모리 주요 아키텍처 패턴 (2025~2026)"
Cohesion: 0.07
Nodes (28): 01. 에이전트 메모리 주요 아키텍처 패턴 (2025~2026), 1. 파일 기반 계층 메모리, 2. OS형 계층 메모리, 3. 추출·통합 메모리 레이어, 4. 시간 인지 지식그래프, 5. 경험·절차 메모리 (self-evolving), 6. RL로 학습된 메모리 관리, 공통 구조 (+20 more)

### Community 49 - "Reference"
Cohesion: 0.29
Nodes (7): Reference, 공식, 논문, 벤치마크 데이터셋, 분석 / 해설, 분석한 오픈소스 코드, 오픈소스 복제 / 큐레이션

### Community 50 - "chatgpt-memory_openai-help-faq.md"
Cohesion: 0.07
Nodes (26): Ask ChatGPT not to mention something, Can ChatGPT remember my name or account identity?, Can memory personalize web searches?, Can memory use files or connected apps?, Can workspace owners control memory?, Correct information, Correct or remove remembered information, Delete remembered information (+18 more)

### Community 58 - "cases/README.md"
Cohesion: 0.16
Nodes (6): How Claude remembers your project (CLAUDE.md / auto memory), Building an agentic memory system for GitHub Copilot, Memory (CrewAI unified memory), Rules, Memory overview (LangGraph: short-term / long-term, semantic·episodic·procedural), Context Engineering for AI Agents: Lessons from Building Manus

### Community 62 - "Build with Supermemory (API)"
Cohesion: 0.08
Nodes (23): API at a glance, Benchmarking your own memory solution, Benchmarks, Build with Supermemory (API), Connectors, Framework integrations, Give your AI memory, How it works (+15 more)

### Community 63 - "memodb-io/memobase README"
Cohesion: 0.09
Nodes (22): 1. Make sure you're connected, 2. Manage Users, 3. Insert Data, 4. Get your Memory, 5. Integrate memory into your prompt, Contribute, Core Features, Documentation (+14 more)

### Community 65 - "Rules"
Cohesion: 0.10
Nodes (21): [Activation and enforcement](#activation-and-enforcement), [AGENTS.md](#agentsmd), [Best practices](#best-practices), [Creating a rule](#creating-a-rule), [Examples](#examples), [FAQ](#faq), [Format and how Team Rules are applied](#format-and-how-team-rules-are-applied), [Glob pattern examples](#glob-pattern-examples) (+13 more)

### Community 66 - "FAQ"
Cohesion: 0.10
Nodes (19): 1. Add AGENTS.md, 2. Cover what matters, 3. Add extra instructions, 4. Large monorepo? Use nested AGENTS.md files for subprojects, About, AGENTS.md, AGENTS.md — A simple, open format for guiding coding agents, Are there required fields? (+11 more)

### Community 67 - "topoteretes/cognee README"
Cohesion: 0.11
Nodes (18): Benchmarks and research, Choose your starting point, Code of Conduct, Community & Support, Connect your agent, Contributing, Deploy Cognee, Explore examples (+10 more)

### Community 70 - "05.agent_memory/docs/index.md"
Cohesion: 0.22
Nodes (7): ABCD (Action-Based Conversations Dataset) 원본, 메모리 관리 / 학습 (RL·test-time), 메모리 아키텍처, 벤치마크, 서베이, 에이전트 메모리 논문 원문 모음, Reference

### Community 71 - "Memory"
Cohesion: 0.12
Nodes (15): Concept, Configuring Memory for an Agent, Custom Chat Store, Customizing Memory, Customizing Memory Blocks, (Deprecated) Memory Types, Examples, Long-Term Memory (+7 more)

### Community 72 - "MemTensor/MemOS README"
Cohesion: 0.12
Nodes (16): 1. MemOS Cloud Plugin, 2. Local Plugin (OpenClaw, Hermes, and DeepSeek Harness), 📚 Citation, 🤝 Community, DeepSeek Harness, Key Features, ⚖️ License, 👾 MemOS: Memory Operating System for LLM & AI Agents (+8 more)

### Community 74 - "Long-term memory"
Cohesion: 0.14
Nodes (14): Collection, Episodic memory, In the background, In the hot path, Learn more, Long-term memory, Manage short-term memory, Memory overview (+6 more)

### Community 75 - "🚀 Quickstart Guide <a name="quickstart"></a>"
Cohesion: 0.14
Nodes (14): Agent Skills, Basic Usage, Citation, CLI, Cloud Platform, 📚 Documentation & Support, 🔗 Integrations & Demos, Introduction (+6 more)

### Community 78 - "Action-Based Conversations Dataset (ABCD)"
Cohesion: 0.15
Nodes (12): Action-Based Conversations Dataset (ABCD), Citation, Contact, Conversation, Data, Evaluation, Guidelines, Introduction (+4 more)

### Community 80 - "자동 문서화 규칙 (필수)"
Cohesion: 0.18
Nodes (9): 디렉터리 구조 변경 시 (AGENTS.md 계층), 문서 구조 (research), 문서 위치 (lab), 문서를 만들거나 옮길 때 (docs/index.md), 실험 결과가 나오거나 보고서를 쓸 때 (docs/report), 자동 문서화 규칙 (필수), 자료를 조사했을 때 (docs/reference), 커밋 시 (docs/worklog 날짜별 로그) — 항상 (+1 more)

### Community 81 - "Effective context engineering for AI agents"
Cohesion: 0.18
Nodes (10): Compaction, Conclusion, Context engineering for long-horizon tasks, Context engineering vs. prompt engineering, Context retrieval and agentic search, Effective context engineering for AI agents, Structured note-taking, Sub-agent architectures (+2 more)

### Community 82 - "About Copilot Memory"
Cohesion: 0.20
Nodes (10): About Copilot Memory, [Benefits of using Copilot Memory](#benefits-of-using-copilot-memory), [Copilot Business and Copilot Enterprise plans](#copilot-business-and-copilot-enterprise-plans), [Enabling Copilot Memory](#enabling-copilot-memory), [Feature availability](#feature-availability), [How Copilot Memory stores, retains, and uses information](#how-copilot-memory-stores-retains-and-uses-information), [Repository-level facts](#repository-level-facts), [Retention and validation](#retention-and-validation) (+2 more)

### Community 83 - "How we built our multi-agent research system"
Cohesion: 0.20
Nodes (9): Appendix, Architecture overview for Research, Benefits of a multi-agent system, Conclusion, Effective evaluation of agents, How we built our multi-agent research system, Production reliability and engineering challenges, Prompt engineering and evaluations for research agents (+1 more)

### Community 84 - "Cascade Memories (Windsurf)"
Cohesion: 0.20
Nodes (9): Best Practices, Cascade Memories (Windsurf), How System Rules Work, How to Manage Memories, Memories, Rules, Rules Discovery, Rules Storage Locations (+1 more)

### Community 85 - "05.agent_memory"
Cohesion: 0.22
Nodes (8): 05.agent_memory, Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory

### Community 86 - "autogen-memory_microsoft-docs.md"
Cohesion: 0.22
Nodes (8): Building a Simple RAG Agent[#](#building-a-simple-rag-agent), Custom Memory Stores (Vector DBs, etc.)[#](#custom-memory-stores-vector-dbs-etc), ListMemory Example[#](#listmemory-example), Mem0Memory Example[#](#mem0memory-example), Memory and RAG (AutoGen AgentChat), Memory and RAG[#](#memory-and-rag), RAG Agent: Putting It All Together[#](#rag-agent-putting-it-all-together), Redis Memory[#](#redis-memory)

### Community 87 - "Memory for agents"
Cohesion: 0.22
Nodes (8): Episodic Memory, How to update memory, Memory for agents, Memory is application-specific, Procedural Memory, Semantic Memory, Types of memory, Why do we care about memory for agents?

### Community 88 - "For AI Agents"
Cohesion: 0.25
Nodes (7): Common Patterns, For AI Agents, Key Files, Purpose, server, Testing Requirements, Working In This Directory

### Community 89 - "Custom instructions with AGENTS.md (Codex)"
Cohesion: 0.25
Nodes (7): Add code review rules, ~/.codex/config.toml, Create global guidance, Custom instructions with AGENTS.md (Codex), Customize fallback filenames, How Codex discovers guidance, Layer project instructions

### Community 90 - "Sleep-time Compute"
Cohesion: 0.25
Nodes (8): Better cost and performance, Conclusion, Configuring sleep-time agents, From test-time scaling to sleep-time scaling, Making machines think while they sleep, MemGPT 2.0: Sleep-time agents in Letta, Sleep-time Compute, The crucial role of memory and state

### Community 91 - "Introducing Copilot Memory: A More Productive and Personalized AI for the Way You Work"
Cohesion: 0.25
Nodes (7): Coming Soon: General Availability, Introducing Copilot Memory: A More Productive and Personalized AI for the Way You Work, Try memory in Copilot, What Copilot Will—and Won’t—Remember, What is memory in Copilot?, Why It Matters, You’re Always in Control

### Community 92 - "Context Engineering for AI Agents: Lessons from Building Manus"
Cohesion: 0.25
Nodes (8): Conclusion, Context Engineering for AI Agents: Lessons from Building Manus, Design Around the KV-Cache, Don't Get Few-Shotted, Keep the Wrong Stuff In, Manipulate Attention Through Recitation, Mask, Don't Remove, Use the File System as Context

### Community 93 - "Managing context on the Claude Developer Platform"
Cohesion: 0.29
Nodes (6): Building long-running agents, Context windows have limits, but real work doesn’t, Getting started, Managing context on the Claude Developer Platform, Managing context on the Claude Developer Platform (context editing + memory tool), Performance improvements with context management

### Community 94 - "Bringing memory to Claude"
Cohesion: 0.29
Nodes (6): Bringing memory to Claude, Bringing memory to Claude, Getting started, Incognito chat, Memory built for work, Starting with teams at work

### Community 95 - "Save info & preferences"
Cohesion: 0.29
Nodes (6): Find, edit, or delete saved info, How to save info, Save info and reference past chats in Gemini Apps, Save info & preferences, Turn personal context on or off, What you need

### Community 96 - "MemFS | Letta Docs (git-versioned memory filesystem)"
Cohesion: 0.29
Nodes (7): Managing memory, MemFS | Letta Docs (git-versioned memory filesystem), Memory structure, Semantic and vector search, Shared memory, Skills in MemFS, Versioning and synchronization

### Community 97 - "Gemini adds Temporary Chats and new personalization features"
Cohesion: 0.33
Nodes (5): Control your data with new settings, Gemini adds Temporary Chats and new personalization features, Gemini adds Temporary Chats and new personalization features, Have quick, one-off chats with Temporary Chat, Use past chats to get more personalized responses

### Community 98 - "Memory | Letta Docs (memory blocks, MemFS, dreaming)"
Cohesion: 0.33
Nodes (6): Dreaming, MemFS, Memory | Letta Docs (memory blocks, MemFS, dreaming), Persona and human shorthand, Setting memory at creation, What to read next

### Community 99 - "Cases — 실제 에이전트 메모리 구현 사례 원문"
Cohesion: 0.33
Nodes (6): 1. 상용 어시스턴트 메모리, 2. 코딩 에이전트 메모리, 3. 오픈소스 메모리 프레임워크/서비스, 4. 엔지니어링 글 (프로덕션 구축기), Cases — 실제 에이전트 메모리 구현 사례 원문, 수집 실패·제외

### Community 100 - "chatgpt-memory_openai-blog.md"
Cohesion: 0.40
Nodes (4): Author, Memory and new controls for ChatGPT, Memory and new controls for ChatGPT, Related articles

### Community 101 - "LangMem"
Cohesion: 0.29
Nodes (6): Creating an Agent, Installation, Key features, langchain-ai/langmem README, LangMem, Next Steps

### Community 102 - "letta_github-readme.md"
Cohesion: 0.40
Nodes (4): Get started, Historical source, Letta, letta-ai/letta README (MemGPT 후신, 현재는 letta-code로 이전 안내)

### Community 103 - "2026_10_28"
Cohesion: 0.40
Nodes (4): 2026_10_28, 메모리 아키텍처 패턴 정리, 에이전트 메모리 설계 비교, 에이전트 메모리 자료 수집 (논문·구축 사례)

### Community 104 - "2026_11_01"
Cohesion: 0.50
Nodes (3): 2026_11_01, CS 챗봇 메모리 구조, 대표 메모리 방법론 동작 다이어그램

### Community 105 - "2026_11_04"
Cohesion: 0.50
Nodes (3): 2026_11_04, CS 챗봇 실험용 샘플 데이터 확보, 메모리 구조 발전 스터디 문서 (통째로 넣기 → RAG → 에이전틱 메모리)

### Community 106 - "mem0_github-readme.md"
Cohesion: 0.50
Nodes (3): mem0ai/mem0 README, New Memory Algorithm (April 2026), Research Highlights

## Ambiguous Edges - Review These
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` → `Independent Top-Level Experiment Folders`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` → `NN.topic Folder Numbering`  [AMBIGUOUS]
  README.md · relation: conceptually_related_to
- `Independent Top-Level Experiment Folders` → `Copy-First, Promote to shared/ After 3 Repeats`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to

## Knowledge Gaps
- **16 isolated node(s):** `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)`, `NanoJev`, `Four-layer license check (code/weights/base/data)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 658 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Memory` connect `Memory` to `cases/README.md`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **What connects `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `new-study Skill` be split into smaller, more focused modules?**
  _Cohesion score 0.10227272727272728 - nodes in this community are weakly interconnected._
- **Why does `getzep/graphiti README (Zep 시간 지식그래프)` connect `getzep/graphiti README (Zep 시간 지식그래프)` to `cases/README.md`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Should `Memory tool` be split into smaller, more focused modules?**
  _Cohesion score 0.046511627906976744 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `Independent Top-Level Experiment Folders`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `NN.topic Folder Numbering`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
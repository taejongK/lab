# Graph Report - lab_npc-engine  (2026-11-05)

## Corpus Check
- 151 files · ~178,712 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 27 file(s) not represented in the graph (top: (none) 25, .graphify-bak 1, .lock 1)

## Summary
- 1527 nodes · 1940 edges · 109 communities (94 shown, 15 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 34 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ea4ad55d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- new-study Skill
- Laya
- Memory tool
- 02.llm_world/docs/reference/README.md
- main.py
- Calibration
- 01.jev/CLAUDE.md
- {기능명} — 로직 인계 문서
- 자동 문서화 규칙 (필수)
- 02.llm_world
- {디렉터리 경로 또는 패키지명}
- {기능명} — 개발 로그
- For AI Agents
- evaluate_composed_maze_nanojev.py
- 01. 아키텍처 (MVP 초안)
- Handover Index
- frontend/README.md
- server/README.md
- server
- unified_grid_envs_nanojev.py
- 공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사
- Memory
- observe_doom-war.py
- 표현 방식 8가지
- arXiv 초록 원문 (NPC·외부 자극 반응 관련)
- UnifiedDoomEnv
- probe_ascii_map.py
- {기능명} — 로직 인계 문서
- {기능명} — 로직 인계 문서
- 결과
- 2026_10_25_spatial-state-encoding.md
- CLAUDE.md files
- 자동 문서화 규칙 (필수)
- 자동 문서화 규칙 (필수)
- analysis_typesafe-snake.ts
- System One 모델로 게임을 플레이하는 방식 — 사례 조사
- Jev
- getzep/graphiti README (Zep 시간 지식그래프)
- Engine
- 03.image_filter
- {디렉터리 경로 또는 패키지명}
- World
- {디렉터리 경로 또는 패키지명}
- prompt_typesafe-snake.ts
- LLM logit readout approach
- DecisionModel.forward
- {기능명} — 개발 로그
- {기능명} — 개발 로그
- 01. 에이전트 메모리 주요 아키텍처 패턴 (2025~2026)
- Reference
- chatgpt-memory_openai-help-faq.md
- Atomic maze judgments and code planning
- Development results: fixed maze and Snake pilot
- Model-guided edge exploration: measured results
- Navigation V3 固定实验报告
- docs
- Handover Index
- cases/README.md
- image_filter
- 2026_10_19.md
- 2026_10_25.md
- Build with Supermemory (API)
- memodb-io/memobase README
- AI TRPG 캐릭터 엔진 — 설계
- Rules
- FAQ
- topoteretes/cognee README
- server.py
- json
- 05.agent_memory/docs/index.md
- Memory
- MemTensor/MemOS README
- 04.npc_engine/README.md
- Long-term memory
- 🚀 Quickstart Guide <a name="quickstart"></a>
- clef_judge.py
- Handler
- Action-Based Conversations Dataset (ABCD)
- FakeAI
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
- mem0ai/mem0 README
- 2026-10-27
- 05.agent_memory/README.md

## God Nodes (most connected - your core abstractions)
1. `World` - 28 edges
2. `Engine` - 27 edges
3. `arXiv 초록 원문 (NPC·외부 자극 반응 관련)` - 21 edges
4. `Memory` - 21 edges
5. `getzep/graphiti README (Zep 시간 지식그래프)` - 19 edges
6. `UnifiedDoomEnv` - 14 edges
7. `play()` - 14 edges
8. `Memory tool` - 14 edges
9. `memodb-io/memobase README` - 14 edges
10. `Jev` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Study README Template` --semantically_similar_to--> `Project README Template (status/period/what-why/results/conclusion)`  [INFERRED] [semantically similar]
  .claude/skills/new-study/template/README.md → README.md
- `결정 사항` --references--> `npc_loop()`  [INFERRED]
  02.llm_world/docs/plan/active/20261013_mvp_devlog.md → 02.llm_world/server/main.py
- `MVP 4단계: NPC 랜덤 목적지 이동` --references--> `npc_loop()`  [INFERRED]
  02.llm_world/docs/worklog/2026_10_13.md → 02.llm_world/server/main.py
- `new-study Skill` --conceptually_related_to--> `01.jev Study`  [INFERRED]
  .claude/skills/new-study/SKILL.md → README.md
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` --conceptually_related_to--> `NN.topic Folder Numbering`  [AMBIGUOUS]
  README.md → .claude/skills/new-study/SKILL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Three implementation lineages of Jev replicas** — 01_jev_docs_notes_02_오픈소스_복제_모델_llm_logit_readout, 01_jev_docs_notes_02_오픈소스_복제_모델_llm_decision_head, 01_jev_docs_notes_02_오픈소스_복제_모델_encoder_head, 01_jev_docs_notes_01_jev_소개와_개념_jev [EXTRACTED 1.00]
- **Jev typed question primitives (Noul/Choice/Score)** — 01_jev_docs_notes_01_jev_소개와_개념_noul, 01_jev_docs_notes_01_jev_소개와_개념_choice, 01_jev_docs_notes_01_jev_소개와_개념_score, 01_jev_docs_notes_03_laya_모델_구조_k_way_reduction [EXTRACTED 1.00]
- **new-study Scaffold Output Files** — _claude_skills_new_study_skill_new_study, _claude_skills_new_study_template_readme_study_readme, _claude_skills_new_study_template_agents_study_agents_md, _claude_skills_new_study_template_claude_auto_doc_rules, _claude_skills_new_study_template_docs_reference_readme_reference_index, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **worklog-discipline Feature Documentation Lifecycle (devlog -> handover -> index)** — _claude_skills_new_study_template_claude_devlog_rule, _claude_skills_new_study_template_claude_handover_rule, _claude_skills_new_study_template_docs_plan_templates_dev_log_template_dev_log_template, _claude_skills_new_study_template_docs_plan_templates_handover_template_handover_template, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **Experiment Isolation Principle** — claude_independent_experiment_folders, readme_self_contained_projects, claude_pep723_uv_run, readme_shared_promotion_rule [INFERRED 0.75]
- **Laya calibration pipeline (RLCD loss, proper scoring, bucket temperature)** — 01_jev_docs_notes_03_laya_모델_구조_rlcd_loss, 01_jev_docs_notes_03_laya_모델_구조_proper_reward, 01_jev_docs_notes_03_laya_모델_구조_temp_bucket, 01_jev_docs_notes_03_laya_모델_구조_answer_confidence, 01_jev_docs_notes_01_jev_소개와_개념_calibration [INFERRED 0.85]

## Communities (109 total, 15 thin omitted)

### Community 0 - "new-study Skill"
Cohesion: 0.10
Nodes (17): new-study Skill, Study Folder Structure (docs/notes, reference, worklog, plan), Study AGENTS.md Template, worklog-discipline Plugin (/init-workstructure), Handover Index, AGENTS_TEMPLATE, DEV_LOG_TEMPLATE, HANDOVER_TEMPLATE (+9 more)

### Community 1 - "Laya"
Cohesion: 0.19
Nodes (15): RLCD (Reinforcement Learning for Calibrated Decisions), decider, Decision Index, Dohnuts, Encoder + head approach, kev, Laya, LLM backbone + trained decision head approach (+7 more)

### Community 2 - "Memory tool"
Cohesion: 0.04
Nodes (43): Basic usage, Context editing integration, create, delete, Directory handling, Directory handling, Directory handling, Directory handling (+35 more)

### Community 3 - "02.llm_world/docs/reference/README.md"
Cohesion: 0.19
Nodes (9): awesome-jev, Four-layer license check (code/weights/base/data), Gneiting & Raftery 2007 (Strictly Proper Scoring Rules), proper_reward (log + spherical + RPS), Shao et al. 2024 DeepSeekMath (GRPO), Williams 1992 (REINFORCE), new-study skill, Legacy Sept research (git 932e704 2026-09-jev/) (+1 more)

### Community 4 - "main.py"
Cohesion: 0.05
Nodes (26): 결정 사항, 02.llm_world 폴더 생성 및 목표 설정, 2026-10-13, MVP 1단계: uzu 스모크 테스트, MVP 2단계: 서버 뼈대, MVP 3단계: 프론트 뼈대, MVP 4단계: NPC 랜덤 목적지 이동, MVP 5단계: LLM 판단 + 고착 문제 3인 논의 (+18 more)

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

### Community 13 - "evaluate_composed_maze_nanojev.py"
Cohesion: 0.06
Nodes (27): describe(), heuristic(), JevBrain, main(), play(), atomic_metrics(), digest(), evaluate_audits() (+19 more)

### Community 14 - "01. 아키텍처 (MVP 초안)"
Cohesion: 0.08
Nodes (21): 01. 아키텍처 (MVP 초안), NPC 판단, 미확인 / 열린 질문, 서버 루프, 월드, 전체 구조, 출처, 프로토콜 (+13 more)

### Community 15 - "Handover Index"
Cohesion: 0.50
Nodes (3): Handover Index, 인계 대기 중, 인계 현황

### Community 19 - "unified_grid_envs_nanojev.py"
Cohesion: 0.12
Nodes (6): _Base, _destination(), _json(), _positive(), UnifiedMazeEnv, UnifiedSnakeEnv

### Community 20 - "공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사"
Cohesion: 0.07
Nodes (26): docs, notes, plan, reference, report, worklog, Handover Index, 인계 대기 중 (+18 more)

### Community 21 - "Memory"
Cohesion: 0.05
Nodes (44): Best Practices for Scope Design, Composite Scoring, Configuration Reference, Crew Shutdown, Discovery, Embedder Configuration, Failure Behavior, Four Ways to Use Memory (+36 more)

### Community 22 - "observe_doom-war.py"
Cohesion: 0.14
Nodes (8): bearing(), clearance(), Contact, Observation, read(), room(), side(), span()

### Community 23 - "표현 방식 8가지"
Cohesion: 0.09
Nodes (22): 1. 화면 좌표 bbox — NanoJev Doom, 2. 전체 격자 ASCII — typesafe-snake, 3. 에이전트 중심 국소 창 + 탐험 기억 — NanoJev Maze, 4. 자기중심 극좌표 (숫자) — jev-plays-doom, 5. 자기중심 극좌표 (구간 단어) — doom-war, doom-jev, 6. 방향별 여유 공간 — doom-war, doom-jev, 7. 1차원 거리 한 줄 — CLM T-Rex, 8. 공간 결과를 선택지 설명에 넣기 — 가장 많이 쓰이고 효과가 큰 방식 (+14 more)

### Community 24 - "arXiv 초록 원문 (NPC·외부 자극 반응 관련)"
Cohesion: 0.10
Nodes (21): A Survey on Large Language Model-Based Game Agents, A Visualized Framework for Event Cooperation with Generative Agents, Affordable Generative Agents, Agents Play Thousands of 3D Video Games, An Empirical Evaluation of AI-Powered Non-Player Characters' Perceived Realism and Performance in Virtual Reality Environments, arXiv 초록 원문 (NPC·외부 자극 반응 관련), Empowering NPC Dialogue with Environmental Context Using LLMs and Panoramic Images, Game Agent Driven by Free-Form Text Command: Using LLM-based Code Generation and Behavior Branch (+13 more)

### Community 25 - "UnifiedDoomEnv"
Cohesion: 0.19
Nodes (4): _finite(), _load_vizdoom(), _positive_int(), UnifiedDoomEnv

### Community 26 - "probe_ascii_map.py"
Cohesion: 0.17
Nodes (13): fetch(), main(), answer_of(), ask_move(), bfs(), criteria(), good_moves(), legal() (+5 more)

### Community 27 - "{기능명} — 로직 인계 문서"
Cohesion: 0.14
Nodes (13): 1단계: {단계명}, 2단계: {단계명}, 개요, 구현 시 주의사항, {기능명} — 로직 인계 문서, 단계별 로직 상세, 데이터 흐름, 설계 결정 사항 (+5 more)

### Community 28 - "{기능명} — 로직 인계 문서"
Cohesion: 0.14
Nodes (13): 1단계: {단계명}, 2단계: {단계명}, 개요, 구현 시 주의사항, {기능명} — 로직 인계 문서, 단계별 로직 상세, 데이터 흐름, 설계 결정 사항 (+5 more)

### Community 29 - "결과"
Cohesion: 0.14
Nodes (14): 1. 서베이 (출발점), 2. 자극 → 판단 구조 (아키텍처), 3. LLM → 실행 가능한 행동 (BT / 코드), 4. 지각 (환경을 어떻게 입력할지), 5. 실시간성 (지연 문제), 6. 평가·사용자 연구, 7. 업계 사례, 결과 (+6 more)

### Community 30 - "2026_10_25_spatial-state-encoding.md"
Cohesion: 0.20
Nodes (6): Reference, V3 导航 2×2 与教师对照：固定协议, 2026_10_27, ASCII 2D 맵 + 오브젝트 설명으로 NPC 이동을 정할 수 있나, System One 모델로 게임을 할 때 공간 정보를 어떻게 넣나, 외부 자극에 반응하는 NPC 관련 최근 3년 자료 조사

### Community 31 - "CLAUDE.md files"
Cohesion: 0.05
Nodes (42): AGENTS.md, Audit and edit your memory, Audit your instruction files, Auto memory, Choose where to put CLAUDE.md files, Choose which instruction files load, Claude ignores the end of my subdirectory CLAUDE.md, Claude isn't following my CLAUDE.md (+34 more)

### Community 32 - "자동 문서화 규칙 (필수)"
Cohesion: 0.18
Nodes (9): 디렉터리 구조 변경 시 (AGENTS.md 계층), 문서 구조 (research), 문서 위치, 문서를 만들거나 옮길 때 (docs/index.md), 실험 결과가 나오거나 보고서를 쓸 때 (docs/report), 자동 문서화 규칙 (필수), 자료를 조사했을 때 (docs/reference), 커밋 시 (docs/worklog 날짜별 로그) — 항상 (+1 more)

### Community 33 - "자동 문서화 규칙 (필수)"
Cohesion: 0.18
Nodes (9): 디렉터리 구조 변경 시 (AGENTS.md 계층), 문서 구조 (research), 문서 위치, 문서를 만들거나 옮길 때 (docs/index.md), 실험 결과가 나오거나 보고서를 쓸 때 (docs/report), 자동 문서화 규칙 (필수), 자료를 조사했을 때 (docs/reference), 커밋 시 (docs/worklog 날짜별 로그) — 항상 (+1 more)

### Community 34 - "analysis_typesafe-snake.ts"
Cohesion: 0.27
Nodes (9): analyze(), analyzeMove(), CLOCKWISE, fallbackMove(), floodFill(), legalMoves(), MoveFacts, Turn (+1 more)

### Community 35 - "System One 모델로 게임을 플레이하는 방식 — 사례 조사"
Cohesion: 0.18
Nodes (11): Snake 예시 — 상하좌우를 고르는 형태, System One 모델로 게임을 플레이하는 방식 — 사례 조사, 결과, 남은 질문, 모델 사용 방식 3가지, 목적, 반복해서 나오는 설계 패턴, 방법 (+3 more)

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

### Community 41 - "World"
Cohesion: 0.07
Nodes (11): 04.npc_engine, Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory (+3 more)

### Community 42 - "{디렉터리 경로 또는 패키지명}"
Cohesion: 0.22
Nodes (8): Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory, {디렉터리 경로 또는 패키지명}

### Community 43 - "prompt_typesafe-snake.ts"
Cohesion: 0.28
Nodes (6): buildRequest(), describeMove(), JevRequest, LEGEND, PRESETS, renderBoard()

### Community 44 - "LLM logit readout approach"
Cohesion: 0.29
Nodes (7): Constrained decoding (null hypothesis), Sean Goedecke skeptical analysis, AnyJev, JevBench, Position (option-order) bias, SemIf (OpenJev), parallel_layout (order-invariant layout, undeployed)

### Community 45 - "DecisionModel.forward"
Cohesion: 0.29
Nodes (5): build_sequence / build_head, DecisionModel.forward, [MASK]-per-option scoring, ModernBERT-large encoder, Warner et al. 2024 (ModernBERT)

### Community 46 - "{기능명} — 개발 로그"
Cohesion: 0.25
Nodes (7): 개발 계획, 결정 사항, {기능명} — 개발 로그, 메모, 목표, 변경 이력, 현재 상태

### Community 47 - "{기능명} — 개발 로그"
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

### Community 51 - "Atomic maze judgments and code planning"
Cohesion: 0.29
Nodes (6): API probability records, Atomic maze judgments and code planning, Fixed-route question benchmark, Frozen local dataset, Matching local training inputs, Model-guided execution

### Community 52 - "Development results: fixed maze and Snake pilot"
Cohesion: 0.29
Nodes (6): Development results: fixed maze and Snake pilot, Independent question and probability measurements, Maze: success / steps, Snake: food score / steps / outcome, Systems and roles, Verification and reproduction

### Community 53 - "Model-guided edge exploration: measured results"
Cohesion: 0.33
Nodes (5): Full-horizon results, Interpretation and verification, Model-guided edge exploration: measured results, Original 128-attempt pilot, retained, System roles

### Community 54 - "Navigation V3 固定实验报告"
Cohesion: 0.33
Nodes (5): Navigation V3 固定实验报告, 固定闭环协议与覆盖, 完整性与来源, 离线 gold 目标与教师拟合分别报告, 预定主模型与配对差值

### Community 55 - "docs"
Cohesion: 0.40
Nodes (5): docs, plan, reference, report, worklog

### Community 56 - "Handover Index"
Cohesion: 0.50
Nodes (3): Handover Index, 인계 대기 중, 인계 현황

### Community 58 - "cases/README.md"
Cohesion: 0.14
Nodes (7): How Claude remembers your project (CLAUDE.md / auto memory), Building an agentic memory system for GitHub Copilot, Memory (CrewAI unified memory), Rules, Memory overview (LangGraph: short-term / long-term, semantic·episodic·procedural), langchain-ai/langmem README, Context Engineering for AI Agents: Lessons from Building Manus

### Community 62 - "Build with Supermemory (API)"
Cohesion: 0.08
Nodes (23): API at a glance, Benchmarking your own memory solution, Benchmarks, Build with Supermemory (API), Connectors, Framework integrations, Give your AI memory, How it works (+15 more)

### Community 63 - "memodb-io/memobase README"
Cohesion: 0.09
Nodes (22): 1. Make sure you're connected, 2. Manage Users, 3. Insert Data, 4. Get your Memory, 5. Integrate memory into your prompt, Contribute, Core Features, Documentation (+14 more)

### Community 64 - "AI TRPG 캐릭터 엔진 — 설계"
Cohesion: 0.10
Nodes (21): 1. 무엇을, 왜, 2. 목표, 3. 역할, 4. 플레이어 조작, 5. 엔진 구조, 6. 첫 시나리오: 성 `[제안]`, 7. 제약과 기술 선택, 8. 검증 `[제안]` (+13 more)

### Community 65 - "Rules"
Cohesion: 0.10
Nodes (21): [Activation and enforcement](#activation-and-enforcement), [AGENTS.md](#agentsmd), [Best practices](#best-practices), [Creating a rule](#creating-a-rule), [Examples](#examples), [FAQ](#faq), [Format and how Team Rules are applied](#format-and-how-team-rules-are-applied), [Glob pattern examples](#glob-pattern-examples) (+13 more)

### Community 66 - "FAQ"
Cohesion: 0.10
Nodes (19): 1. Add AGENTS.md, 2. Cover what matters, 3. Add extra instructions, 4. Large monorepo? Use nested AGENTS.md files for subprojects, About, AGENTS.md, AGENTS.md — A simple, open format for guiding coding agents, Are there required fields? (+11 more)

### Community 67 - "topoteretes/cognee README"
Cohesion: 0.11
Nodes (17): Benchmarks and research, Choose your starting point, Code of Conduct, Community & Support, Connect your agent, Contributing, Deploy Cognee, Explore examples (+9 more)

### Community 69 - "json"
Cohesion: 0.23
Nodes (8): ClaudeAI, AIError, check_fake(), ask(), check_rules(), run_real(), teleport(), load_scenario()

### Community 70 - "05.agent_memory/docs/index.md"
Cohesion: 0.14
Nodes (12): docs, notes, reference, report, worklog, ABCD (Action-Based Conversations Dataset) 원본, 메모리 관리 / 학습 (RL·test-time), 메모리 아키텍처 (+4 more)

### Community 71 - "Memory"
Cohesion: 0.12
Nodes (15): Concept, Configuring Memory for an Agent, Custom Chat Store, Customizing Memory, Customizing Memory Blocks, (Deprecated) Memory Types, Examples, Long-Term Memory (+7 more)

### Community 72 - "MemTensor/MemOS README"
Cohesion: 0.12
Nodes (16): 1. MemOS Cloud Plugin, 2. Local Plugin (OpenClaw, Hermes, and DeepSeek Harness), 📚 Citation, 🤝 Community, DeepSeek Harness, Key Features, ⚖️ License, 👾 MemOS: Memory Operating System for LLM & AI Agents (+8 more)

### Community 73 - "04.npc_engine/README.md"
Cohesion: 0.15
Nodes (10): AI TRPG 캐릭터 엔진 — 구현 계획, 단계, 주의할 입력, 파일과 책임, 2026_11_05, 왕 독살 장면을 돌리는 엔진 첫 버전 구현, 캐릭터 엔진의 방향과 첫 버전 범위 정의, NPC Engine (+2 more)

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
Cohesion: 0.40
Nodes (5): Creating an Agent, Installation, Key features, LangMem, Next Steps

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

### Community 106 - "mem0ai/mem0 README"
Cohesion: 0.67
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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 915 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `World` connect `World` to `server.py`, `json`, `Engine`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **What connects `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `new-study Skill` be split into smaller, more focused modules?**
  _Cohesion score 0.10227272727272728 - nodes in this community are weakly interconnected._
- **Why does `Memory` connect `Memory` to `World`, `cases/README.md`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Should `Memory tool` be split into smaller, more focused modules?**
  _Cohesion score 0.044444444444444446 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `Independent Top-Level Experiment Folders`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `NN.topic Folder Numbering`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
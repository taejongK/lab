# Graph Report - lab  (2026-10-27)

## Corpus Check
- 90 files · ~51,222 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 22 file(s) not represented in the graph (top: (none) 20, .graphify-bak 1, .lock 1)

## Summary
- 732 nodes · 1012 edges · 62 communities (54 shown, 8 thin omitted)
- Extraction: 96% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 34 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `93d7014b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- new-study Skill
- Laya
- World
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
- evaluate_composed_maze_nanojev.py
- LLM World
- Handover Index
- frontend/README.md
- server/README.md
- server
- unified_grid_envs_nanojev.py
- 공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사
- doom_agent_jev-plays-doom.py
- observe_doom-war.py
- 표현 방식 8가지
- arXiv 초록 원문 (NPC·외부 자극 반응 관련)
- UnifiedDoomEnv
- probe_ascii_map.py
- {기능명} — 로직 인계 문서
- {기능명} — 로직 인계 문서
- 결과
- 2026_10_25_spatial-state-encoding.md
- state_serializer_doom-jev.py
- 자동 문서화 규칙 (필수)
- 자동 문서화 규칙 (필수)
- analysis_typesafe-snake.ts
- System One 모델로 게임을 플레이하는 방식 — 사례 조사
- Jev
- .say
- 2026-10-13
- 03.image_filter
- {디렉터리 경로 또는 패키지명}
- 04.npc_engine
- {디렉터리 경로 또는 패키지명}
- prompt_typesafe-snake.ts
- LLM logit readout approach
- DecisionModel.forward
- {기능명} — 개발 로그
- {기능명} — 개발 로그
- 02.llm_world/docs/reference/README.md
- Reference
- 01. 아키텍처 (MVP 초안)
- Atomic maze judgments and code planning
- Development results: fixed maze and Snake pilot
- Model-guided edge exploration: measured results
- Navigation V3 固定实验报告
- docs
- Handover Index
- 2026_10_27
- image_filter
- 2026_10_19.md
- 2026_10_25.md

## God Nodes (most connected - your core abstractions)
1. `arXiv 초록 원문 (NPC·외부 자극 반응 관련)` - 21 edges
2. `UnifiedDoomEnv` - 14 edges
3. `Jev` - 14 edges
4. `UnifiedMazeEnv` - 13 edges
5. `main()` - 13 edges
6. `2026-10-13` - 12 edges
7. `decide()` - 11 edges
8. `_Base` - 11 edges
9. `World` - 10 edges
10. `read()` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Study README Template` --semantically_similar_to--> `Project README Template (status/period/what-why/results/conclusion)`  [INFERRED] [semantically similar]
  .claude/skills/new-study/template/README.md → README.md
- `MVP 5단계: LLM 판단 + 고착 문제 3인 논의` --references--> `decide()`  [INFERRED]
  02.llm_world/docs/worklog/2026_10_13.md → 02.llm_world/server/main.py
- `Key Files` --references--> `World`  [INFERRED]
  02.llm_world/server/AGENTS.md → 02.llm_world/server/main.py
- `결정 사항` --references--> `npc_loop()`  [INFERRED]
  02.llm_world/docs/plan/active/20261013_mvp_devlog.md → 02.llm_world/server/main.py
- `new-study Skill` --conceptually_related_to--> `01.jev Study`  [INFERRED]
  .claude/skills/new-study/SKILL.md → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Three implementation lineages of Jev replicas** — 01_jev_docs_notes_02_오픈소스_복제_모델_llm_logit_readout, 01_jev_docs_notes_02_오픈소스_복제_모델_llm_decision_head, 01_jev_docs_notes_02_오픈소스_복제_모델_encoder_head, 01_jev_docs_notes_01_jev_소개와_개념_jev [EXTRACTED 1.00]
- **Jev typed question primitives (Noul/Choice/Score)** — 01_jev_docs_notes_01_jev_소개와_개념_noul, 01_jev_docs_notes_01_jev_소개와_개념_choice, 01_jev_docs_notes_01_jev_소개와_개념_score, 01_jev_docs_notes_03_laya_모델_구조_k_way_reduction [EXTRACTED 1.00]
- **new-study Scaffold Output Files** — _claude_skills_new_study_skill_new_study, _claude_skills_new_study_template_readme_study_readme, _claude_skills_new_study_template_agents_study_agents_md, _claude_skills_new_study_template_claude_auto_doc_rules, _claude_skills_new_study_template_docs_reference_readme_reference_index, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **worklog-discipline Feature Documentation Lifecycle (devlog -> handover -> index)** — _claude_skills_new_study_template_claude_devlog_rule, _claude_skills_new_study_template_claude_handover_rule, _claude_skills_new_study_template_docs_plan_templates_dev_log_template_dev_log_template, _claude_skills_new_study_template_docs_plan_templates_handover_template_handover_template, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **Experiment Isolation Principle** — claude_independent_experiment_folders, readme_self_contained_projects, claude_pep723_uv_run, readme_shared_promotion_rule [INFERRED 0.75]
- **Laya calibration pipeline (RLCD loss, proper scoring, bucket temperature)** — 01_jev_docs_notes_03_laya_모델_구조_rlcd_loss, 01_jev_docs_notes_03_laya_모델_구조_proper_reward, 01_jev_docs_notes_03_laya_모델_구조_temp_bucket, 01_jev_docs_notes_03_laya_모델_구조_answer_confidence, 01_jev_docs_notes_01_jev_소개와_개념_calibration [INFERRED 0.85]

## Communities (62 total, 8 thin omitted)

### Community 0 - "new-study Skill"
Cohesion: 0.10
Nodes (17): new-study Skill, Study Folder Structure (docs/notes, reference, worklog, plan), Study AGENTS.md Template, worklog-discipline Plugin (/init-workstructure), Handover Index, AGENTS_TEMPLATE, DEV_LOG_TEMPLATE, HANDOVER_TEMPLATE (+9 more)

### Community 1 - "Laya"
Cohesion: 0.19
Nodes (15): RLCD (Reinforcement Learning for Calibrated Decisions), decider, Decision Index, Dohnuts, Encoder + head approach, kev, Laya, LLM backbone + trained decision head approach (+7 more)

### Community 2 - "World"
Cohesion: 0.21
Nodes (5): MVP 2단계: 서버 뼈대, MVP 3단계: 프론트 뼈대, bfs(), walkable(), World

### Community 3 - "01.jev/docs/notes/02.오픈소스-복제-모델.md"
Cohesion: 0.31
Nodes (4): awesome-jev, Four-layer license check (code/weights/base/data), new-study skill, Legacy Sept research (git 932e704 2026-09-jev/)

### Community 4 - "main.py"
Cohesion: 0.08
Nodes (19): 결정 사항, MVP 4단계: NPC 랜덤 목적지 이동, Common Patterns, For AI Agents, Key Files, Purpose, server, Testing Requirements (+11 more)

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
Cohesion: 0.07
Nodes (18): judge(), atomic_metrics(), digest(), evaluate_audits(), file_digest(), local_questions(), local_truth(), main() (+10 more)

### Community 14 - "LLM World"
Cohesion: 0.20
Nodes (7): LLM World, 구성, 목표, 문서, 범위 밖 (지금은), 스택, 완료 기준 (MVP)

### Community 15 - "Handover Index"
Cohesion: 0.50
Nodes (3): Handover Index, 인계 대기 중, 인계 현황

### Community 19 - "unified_grid_envs_nanojev.py"
Cohesion: 0.12
Nodes (6): _Base, _destination(), _json(), _positive(), UnifiedMazeEnv, UnifiedSnakeEnv

### Community 20 - "공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사"
Cohesion: 0.07
Nodes (26): docs, notes, plan, reference, report, worklog, Handover Index, 인계 대기 중 (+18 more)

### Community 21 - "doom_agent_jev-plays-doom.py"
Cohesion: 0.13
Nodes (7): fetch(), main(), describe(), heuristic(), JevBrain, main(), play()

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
Cohesion: 0.26
Nodes (3): _finite(), _positive_int(), UnifiedDoomEnv

### Community 26 - "probe_ascii_map.py"
Cohesion: 0.29
Nodes (11): answer_of(), ask_move(), bfs(), criteria(), good_moves(), legal(), main(), make_world() (+3 more)

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
Cohesion: 0.24
Nodes (4): Reference, V3 导航 2×2 与教师对照：固定协议, NPC Engine, 문서

### Community 31 - "state_serializer_doom-jev.py"
Cohesion: 0.26
Nodes (6): detect_walls(), cast_ray(), discretize_bearing(), discretize_distance(), _ray_line_intersect(), serialize_state()

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

### Community 37 - ".say"
Cohesion: 0.22
Nodes (8): 프로토콜, MVP — 개발 로그, 개발 계획, 메모, 목표, 변경 이력, 현재 상태, MVP 6단계: 대화 (말풍선·기억)

### Community 38 - "2026-10-13"
Cohesion: 0.22
Nodes (8): 02.llm_world 폴더 생성 및 목표 설정, 2026-10-13, MVP 1단계: uzu 스모크 테스트, MVP 5단계: LLM 판단 + 고착 문제 3인 논의, MVP 7단계: 도트 그래픽, 개발 전 규칙·문서 세팅, 기술 스택 결정 반영, 스택 확정: 도트 Canvas 2D, WebSocket, Qwen 3.5 0.8B

### Community 39 - "03.image_filter"
Cohesion: 0.22
Nodes (8): 03.image_filter, Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory

### Community 40 - "{디렉터리 경로 또는 패키지명}"
Cohesion: 0.22
Nodes (8): Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory, {디렉터리 경로 또는 패키지명}

### Community 41 - "04.npc_engine"
Cohesion: 0.22
Nodes (8): 04.npc_engine, Common Patterns, For AI Agents, Key Files, Purpose, Subdirectories, Testing Requirements, Working In This Directory

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

### Community 48 - "02.llm_world/docs/reference/README.md"
Cohesion: 0.38
Nodes (5): Gneiting & Raftery 2007 (Strictly Proper Scoring Rules), proper_reward (log + spherical + RPS), Shao et al. 2024 DeepSeekMath (GRPO), Williams 1992 (REINFORCE), Reference

### Community 49 - "Reference"
Cohesion: 0.29
Nodes (7): Reference, 공식, 논문, 벤치마크 데이터셋, 분석 / 해설, 분석한 오픈소스 코드, 오픈소스 복제 / 큐레이션

### Community 50 - "01. 아키텍처 (MVP 초안)"
Cohesion: 0.29
Nodes (7): 01. 아키텍처 (MVP 초안), NPC 판단, 미확인 / 열린 질문, 서버 루프, 월드, 전체 구조, 출처

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
Cohesion: 0.50
Nodes (4): docs, reference, report, worklog

### Community 56 - "Handover Index"
Cohesion: 0.50
Nodes (3): Handover Index, 인계 대기 중, 인계 현황

### Community 58 - "2026_10_27"
Cohesion: 0.50
Nodes (4): 2026_10_27, ASCII 2D 맵 + 오브젝트 설명으로 NPC 이동을 정할 수 있나, System One 모델로 게임을 할 때 공간 정보를 어떻게 넣나, 외부 자극에 반응하는 NPC 관련 최근 3년 자료 조사

## Ambiguous Edges - Review These
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` → `Independent Top-Level Experiment Folders`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` → `NN.topic Folder Numbering`  [AMBIGUOUS]
  README.md · relation: conceptually_related_to
- `Independent Top-Level Experiment Folders` → `Copy-First, Promote to shared/ After 3 Repeats`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to

## Knowledge Gaps
- **16 isolated node(s):** `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)`, `Kahneman Dual-Process Theory (System 1/System 2)`, `Jev suitability 6-question checklist` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 372 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `System One 모델로 게임을 플레이하는 방식 — 사례 조사` connect `System One 모델로 게임을 플레이하는 방식 — 사례 조사` to `2026_10_25_spatial-state-encoding.md`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **What connects `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `new-study Skill` be split into smaller, more focused modules?**
  _Cohesion score 0.10227272727272728 - nodes in this community are weakly interconnected._
- **Why does `해석 — NPC 엔진에 적용하면` connect `System One 모델로 게임을 플레이하는 방식 — 사례 조사` to `World`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Should `main.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08108108108108109 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `Independent Top-Level Experiment Folders`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `NN.topic Folder Numbering`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
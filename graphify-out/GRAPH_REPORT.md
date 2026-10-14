# Graph Report - lab  (2026-10-13)

## Corpus Check
- 44 files · ~17,969 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 8, .graphify-bak 1, .lock 1)

## Summary
- 266 nodes · 364 edges · 19 communities (15 shown, 4 thin omitted)
- Extraction: 90% EXTRACTED · 9% INFERRED · 1% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `58ca74d2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- new-study Skill
- Jev
- 2026-10-13
- reference/README.md
- main.py
- Calibration
- 01.jev/CLAUDE.md
- {기능명} — 로직 인계 문서
- 자동 문서화 규칙 (필수)
- 02.llm_world
- {디렉터리 경로 또는 패키지명}
- {기능명} — 개발 로그
- For AI Agents
- For AI Agents
- LLM World
- Handover Index
- frontend/README.md
- server/README.md
- server

## God Nodes (most connected - your core abstractions)
1. `Jev` - 14 edges
2. `2026-10-13` - 12 edges
3. `decide()` - 11 edges
4. `World` - 10 edges
5. `new-study Skill` - 10 edges
6. `Laya` - 9 edges
7. `자동 문서화 규칙 (필수)` - 8 edges
8. `01. 아키텍처 (MVP 초안)` - 8 edges
9. `{기능명} — 로직 인계 문서` - 8 edges
10. `npc_loop()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Study README Template` --semantically_similar_to--> `Project README Template (status/period/what-why/results/conclusion)`  [INFERRED] [semantically similar]
  .claude/skills/new-study/template/README.md → README.md
- `Key Files` --references--> `World`  [INFERRED]
  02.llm_world/server/AGENTS.md → 02.llm_world/server/main.py
- `MVP 5단계: LLM 판단 + 고착 문제 3인 논의` --references--> `decide()`  [INFERRED]
  02.llm_world/docs/worklog/2026_10_13.md → 02.llm_world/server/main.py
- `Key Files` --references--> `decide()`  [INFERRED]
  02.llm_world/server/AGENTS.md → 02.llm_world/server/main.py
- `결정 사항` --references--> `npc_loop()`  [INFERRED]
  02.llm_world/docs/plan/active/20261013_mvp_devlog.md → 02.llm_world/server/main.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Three implementation lineages of Jev replicas** — 01_jev_docs_notes_02_오픈소스_복제_모델_llm_logit_readout, 01_jev_docs_notes_02_오픈소스_복제_모델_llm_decision_head, 01_jev_docs_notes_02_오픈소스_복제_모델_encoder_head, 01_jev_docs_notes_01_jev_소개와_개념_jev [EXTRACTED 1.00]
- **Jev typed question primitives (Noul/Choice/Score)** — 01_jev_docs_notes_01_jev_소개와_개념_noul, 01_jev_docs_notes_01_jev_소개와_개념_choice, 01_jev_docs_notes_01_jev_소개와_개념_score, 01_jev_docs_notes_03_laya_모델_구조_k_way_reduction [EXTRACTED 1.00]
- **new-study Scaffold Output Files** — _claude_skills_new_study_skill_new_study, _claude_skills_new_study_template_readme_study_readme, _claude_skills_new_study_template_agents_study_agents_md, _claude_skills_new_study_template_claude_auto_doc_rules, _claude_skills_new_study_template_docs_reference_readme_reference_index, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **worklog-discipline Feature Documentation Lifecycle (devlog -> handover -> index)** — _claude_skills_new_study_template_claude_devlog_rule, _claude_skills_new_study_template_claude_handover_rule, _claude_skills_new_study_template_docs_plan_templates_dev_log_template_dev_log_template, _claude_skills_new_study_template_docs_plan_templates_handover_template_handover_template, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **Experiment Isolation Principle** — claude_independent_experiment_folders, readme_self_contained_projects, claude_pep723_uv_run, readme_shared_promotion_rule [INFERRED 0.75]
- **Laya calibration pipeline (RLCD loss, proper scoring, bucket temperature)** — 01_jev_docs_notes_03_laya_모델_구조_rlcd_loss, 01_jev_docs_notes_03_laya_모델_구조_proper_reward, 01_jev_docs_notes_03_laya_모델_구조_temp_bucket, 01_jev_docs_notes_03_laya_모델_구조_answer_confidence, 01_jev_docs_notes_01_jev_소개와_개념_calibration [INFERRED 0.85]

## Communities (19 total, 4 thin omitted)

### Community 0 - "new-study Skill"
Cohesion: 0.10
Nodes (17): new-study Skill, Study Folder Structure (docs/notes, reference, worklog, plan), Study AGENTS.md Template, worklog-discipline Plugin (/init-workstructure), Handover Index, AGENTS_TEMPLATE, DEV_LOG_TEMPLATE, HANDOVER_TEMPLATE (+9 more)

### Community 1 - "Jev"
Cohesion: 0.07
Nodes (35): Choice primitive (up to 255 options), Constrained decoding (null hypothesis), Jev, Kahneman Dual-Process Theory (System 1/System 2), Noul primitive (yes/no), RLCD (Reinforcement Learning for Calibrated Decisions), Score primitive (ordered scale), Sean Goedecke skeptical analysis (+27 more)

### Community 2 - "2026-10-13"
Cohesion: 0.06
Nodes (27): 01. 아키텍처 (MVP 초안), NPC 판단, 미확인 / 열린 질문, 서버 루프, 월드, 전체 구조, 출처, 프로토콜 (+19 more)

### Community 3 - "reference/README.md"
Cohesion: 0.21
Nodes (9): awesome-jev, Four-layer license check (code/weights/base/data), Gneiting & Raftery 2007 (Strictly Proper Scoring Rules), proper_reward (log + spherical + RPS), Shao et al. 2024 DeepSeekMath (GRPO), Williams 1992 (REINFORCE), new-study skill, Legacy Sept research (git 932e704 2026-09-jev/) (+1 more)

### Community 4 - "main.py"
Cohesion: 0.10
Nodes (13): 결정 사항, MVP 4단계: NPC 랜덤 목적지 이동, MVP 5단계: LLM 판단 + 고착 문제 3인 논의, ask(), load(), decide(), lifespan(), nearest_place() (+5 more)

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

### Community 13 - "For AI Agents"
Cohesion: 0.25
Nodes (7): Common Patterns, For AI Agents, Key Files, Purpose, server, Testing Requirements, Working In This Directory

### Community 14 - "LLM World"
Cohesion: 0.29
Nodes (7): LLM World, 구성, 목표, 문서, 범위 밖 (지금은), 스택, 완료 기준 (MVP)

### Community 15 - "Handover Index"
Cohesion: 0.50
Nodes (3): Handover Index, 인계 대기 중, 인계 현황

## Ambiguous Edges - Review These
- `NN.topic Folder Numbering` → `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)`  [AMBIGUOUS]
  README.md · relation: conceptually_related_to
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` → `Independent Top-Level Experiment Folders`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to
- `Independent Top-Level Experiment Folders` → `Copy-First, Promote to shared/ After 3 Repeats`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to

## Knowledge Gaps
- **16 isolated node(s):** `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)`, `Kahneman Dual-Process Theory (System 1/System 2)`, `Jev suitability 6-question checklist` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 111 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `World` connect `2026-10-13` to `main.py`, `For AI Agents`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `decide()` (e.g. with `MVP 4단계: NPC 랜덤 목적지 이동` and `MVP 5단계: LLM 판단 + 고착 문제 3인 논의`) actually correct?**
  _`decide()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `server`, `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `new-study Skill` be split into smaller, more focused modules?**
  _Cohesion score 0.10227272727272728 - nodes in this community are weakly interconnected._
- **Why does `Jev` connect `Jev` to `reference/README.md`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `NN.topic Folder Numbering` and `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` and `Independent Top-Level Experiment Folders`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
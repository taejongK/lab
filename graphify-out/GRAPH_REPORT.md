# Graph Report - lab  (2026-10-11)

## Corpus Check
- Corpus is ~11,131 words - fits in a single context window. You may not need a graph.

## Summary
- 107 nodes · 173 edges · 8 communities (7 shown, 1 thin omitted)
- Extraction: 91% EXTRACTED · 8% INFERRED · 2% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.85)
- Token cost: 169,534 input · 7,000 output

## Community Hubs (Navigation)
- Study Scaffolding & Doc Rules
- Jev Concept & Critique
- Open-Source Jev Replicas
- Jev Notes & Citations
- Lab Repo Conventions
- Calibration & Confidence Routing
- 01.jev Worklog Setup
- Laya Encoder Architecture

## God Nodes (most connected - your core abstractions)
1. `Jev` - 14 edges
2. `new-study Skill` - 10 edges
3. `Laya` - 9 edges
4. `Study AGENTS.md Template` - 7 edges
5. `worklog-discipline Auto-Documentation Rules` - 7 edges
6. `LLM logit readout approach` - 7 edges
7. `Study README Template` - 6 edges
8. `Calibration` - 6 edges
9. `LLM backbone + trained decision head approach` - 6 edges
10. `Independent Top-Level Experiment Folders` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Study README Template` --semantically_similar_to--> `Project README Template (status/period/what-why/results/conclusion)`  [INFERRED] [semantically similar]
  .claude/skills/new-study/template/README.md → README.md
- `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)` --conceptually_related_to--> `NN.topic Folder Numbering`  [AMBIGUOUS]
  README.md → .claude/skills/new-study/SKILL.md
- `new-study Skill` --conceptually_related_to--> `01.jev Study`  [INFERRED]
  .claude/skills/new-study/SKILL.md → README.md
- `Study AGENTS.md Template` --references--> `Disposable Code by Default`  [EXTRACTED]
  .claude/skills/new-study/template/AGENTS.md → CLAUDE.md
- `Study README Template` --implements--> `New Experiment Convention (NN.topic via /new-study)`  [INFERRED]
  .claude/skills/new-study/template/README.md → CLAUDE.md

## Hyperedges (group relationships)
- **worklog-discipline Feature Documentation Lifecycle (devlog -> handover -> index)** — _claude_skills_new_study_template_claude_devlog_rule, _claude_skills_new_study_template_claude_handover_rule, _claude_skills_new_study_template_docs_plan_templates_dev_log_template_dev_log_template, _claude_skills_new_study_template_docs_plan_templates_handover_template_handover_template, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **new-study Scaffold Output Files** — _claude_skills_new_study_skill_new_study, _claude_skills_new_study_template_readme_study_readme, _claude_skills_new_study_template_agents_study_agents_md, _claude_skills_new_study_template_claude_auto_doc_rules, _claude_skills_new_study_template_docs_reference_readme_reference_index, _claude_skills_new_study_template_docs_plan_handover_index_handover_index [EXTRACTED 1.00]
- **Experiment Isolation Principle** — claude_independent_experiment_folders, readme_self_contained_projects, claude_pep723_uv_run, readme_shared_promotion_rule [INFERRED 0.75]
- **Jev typed question primitives (Noul/Choice/Score)** — 01_jev_docs_notes_01_jev_소개와_개념_noul, 01_jev_docs_notes_01_jev_소개와_개념_choice, 01_jev_docs_notes_01_jev_소개와_개념_score, 01_jev_docs_notes_03_laya_모델_구조_k_way_reduction [EXTRACTED 1.00]
- **Three implementation lineages of Jev replicas** — 01_jev_docs_notes_02_오픈소스_복제_모델_llm_logit_readout, 01_jev_docs_notes_02_오픈소스_복제_모델_llm_decision_head, 01_jev_docs_notes_02_오픈소스_복제_모델_encoder_head, 01_jev_docs_notes_01_jev_소개와_개념_jev [EXTRACTED 1.00]
- **Laya calibration pipeline (RLCD loss, proper scoring, bucket temperature)** — 01_jev_docs_notes_03_laya_모델_구조_rlcd_loss, 01_jev_docs_notes_03_laya_모델_구조_proper_reward, 01_jev_docs_notes_03_laya_모델_구조_temp_bucket, 01_jev_docs_notes_03_laya_모델_구조_answer_confidence, 01_jev_docs_notes_01_jev_소개와_개념_calibration [INFERRED 0.85]

## Communities (8 total, 1 thin omitted)

### Community 0 - "Study Scaffolding & Doc Rules"
Cohesion: 0.16
Nodes (10): new-study Skill, Study Folder Structure (docs/notes, reference, worklog, plan), worklog-discipline Plugin (/init-workstructure), Handover Index, DEV_LOG_TEMPLATE, HANDOVER_TEMPLATE, Reference Index (external materials), Study README Template (+2 more)

### Community 1 - "Jev Concept & Critique"
Cohesion: 0.14
Nodes (15): Choice primitive (up to 255 options), Constrained decoding (null hypothesis), Jev, Kahneman Dual-Process Theory (System 1/System 2), Noul primitive (yes/no), Score primitive (ordered scale), Sean Goedecke skeptical analysis, Jev suitability 6-question checklist (+7 more)

### Community 2 - "Open-Source Jev Replicas"
Cohesion: 0.19
Nodes (15): RLCD (Reinforcement Learning for Calibrated Decisions), decider, Decision Index, Dohnuts, Encoder + head approach, kev, Laya, LLM backbone + trained decision head approach (+7 more)

### Community 3 - "Jev Notes & Citations"
Cohesion: 0.23
Nodes (8): awesome-jev, Four-layer license check (code/weights/base/data), Gneiting & Raftery 2007 (Strictly Proper Scoring Rules), proper_reward (log + spherical + RPS), Shao et al. 2024 DeepSeekMath (GRPO), Williams 1992 (REINFORCE), new-study skill, Legacy Sept research (git 932e704 2026-09-jev/)

### Community 4 - "Lab Repo Conventions"
Cohesion: 0.22
Nodes (7): Study AGENTS.md Template, AGENTS_TEMPLATE, lab Repository Rules, PEP 723 Inline Metadata + uv run, Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates), lab Experiment Monorepo, Project README Template (status/period/what-why/results/conclusion)

### Community 5 - "Calibration & Confidence Routing"
Cohesion: 0.22
Nodes (8): Confidence-threshold routing (auto / human review / reasoning LLM), ECE (Expected Calibration Error), Post-hoc temperature scaling, Act head (act/escalate), answer_confidence vs normalized-entropy confidence, _decode_answers, Guo et al. 2017 (On Calibration of Modern Neural Networks), Per-bucket temperature (temp_bucket)

### Community 7 - "Laya Encoder Architecture"
Cohesion: 0.29
Nodes (5): build_sequence / build_head, DecisionModel.forward, [MASK]-per-option scoring, ModernBERT-large encoder, Warner et al. 2024 (ModernBERT)

## Ambiguous Edges - Review These
- `NN.topic Folder Numbering` → `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)`  [AMBIGUOUS]
  README.md · relation: conceptually_related_to
- `Independent Top-Level Experiment Folders` → `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to
- `Independent Top-Level Experiment Folders` → `Copy-First, Promote to shared/ After 3 Repeats`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to

## Knowledge Gaps
- **15 isolated node(s):** `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)`, `TypeSafe AI`, `Kahneman Dual-Process Theory (System 1/System 2)`, `ECE (Expected Calibration Error)` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 17 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Jev` connect `Jev Concept & Critique` to `Open-Source Jev Replicas`, `Jev Notes & Citations`, `Laya Encoder Architecture`?**
  _High betweenness centrality (0.183) - this node is a cross-community bridge._
- **What connects `Study Folder Structure (docs/notes, reference, worklog, plan)`, `worklog-discipline Plugin (/init-workstructure)`, `TypeSafe AI` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Jev Concept & Critique` be split into smaller, more focused modules?**
  _Cohesion score 0.13725490196078433 - nodes in this community are weakly interconnected._
- **Why does `Laya` connect `Open-Source Jev Replicas` to `Jev Concept & Critique`, `Jev Notes & Citations`, `Laya Encoder Architecture`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `NN.topic Folder Numbering` and `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Independent Top-Level Experiment Folders` and `Category Directory Layout (papers/implementations/experiments/prototypes/notes/shared/templates)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Independent Top-Level Experiment Folders` and `Copy-First, Promote to shared/ After 3 Repeats`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
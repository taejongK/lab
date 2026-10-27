# Memp: Exploring Agent Procedural Memory

- 저자: Runnan Fang, Yuan Liang, Xiaobin Wang, Jialong Wu et al.
- 날짜: 2025-08-08 (arXiv v1 제출일, 수집 버전 2508.06433v4)
- 학회/저널: (arXiv comment) ACL 2026 Findings
- arXiv: https://arxiv.org/abs/2508.06433
- 코드: https://github.com/zjunlp/MemP
- 분류: architecture
- 비고: procedural memory
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large Language Models (LLMs) based agents excel at diverse tasks, yet they suffer from brittle procedural memory that is manually engineered or entangled in static parameters. In this work, we investigate strategies to endow agents with a learnable, updatable, and lifelong procedural memory. We propose Memp that distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions, and explore the impact of different strategies for Build, Retrieval, and Update of procedural memory. Coupled with a dynamic regimen that continuously updates, corrects, and deprecates its contents, this repository evolves in lockstep with new experience. Empirical evaluation on TravelPlanner and ALFWorld shows that as the memory repository is refined, agents achieve steadily higher success rates and greater efficiency on analogous tasks. Moreover, procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model can also yield substantial performance gains. Code is available at https://github.com/zjunlp/MemP.

# MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent

- 저자: Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie Chen et al.
- 날짜: 2025-07-03 (arXiv v1 제출일, 수집 버전 2507.02259v2)
- 학회/저널: International Conference on Learning Representations (ICLR), 2026
- arXiv: https://arxiv.org/abs/2507.02259
- 코드: https://github.com/BytedTsinghua-SIA/MemAgent
- 분류: training
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Despite improvements by length extrapolation, efficient attention and memory modules, handling infinitely long documents with linear complexity without performance degradation during extrapolation remains the ultimate challenge in long-text processing. We directly optimize for long-text tasks in an end-to-end fashion and introduce a novel agent workflow, MemAgent, which reads text in segments and updates the memory using an overwrite strategy. We extend the DAPO algorithm to facilitate training via independent-context multi-conversation generation. MemAgent has demonstrated superb long-context capabilities, being able to extrapolate from an 8K context trained on 32K text to a 3.5M QA task with performance loss < 5% and achieves 95%+ in 512K RULER test.

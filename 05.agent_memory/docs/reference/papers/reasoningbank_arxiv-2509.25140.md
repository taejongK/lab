# ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

- 저자: Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen et al.
- 날짜: 2025-09-29 (arXiv v1 제출일, 수집 버전 2509.25140v2)
- 학회/저널: (arXiv comment) Accepted to ICLR 2026; Code: https://github.com/google-research/reasoning-bank
- arXiv: https://arxiv.org/abs/2509.25140
- 코드: https://github.com/google-research/reasoning-bank
- 분류: training
- 비고: test-time memory, no weight update
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arise. Our code can be found at https://github.com/google-research/reasoning-bank.

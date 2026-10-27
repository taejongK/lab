# A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents

- 저자: Wei-Chieh Huang, Weizhi Zhang, Yueqing Liang, Yuanchen Bei et al.
- 날짜: 2026-01-14 (arXiv v1 제출일, 수집 버전 2602.06052v4)
- 학회/저널: (arXiv comment) Accepted at Transactions on Machine Learning Research (TMLR) with Survey Certification. Project page: https://github.com/AgentMemoryWorld/Awesome-Agent-Memory
- arXiv: https://arxiv.org/abs/2602.06052
- 코드: https://github.com/AgentMemoryWorld/Awesome-Agent-Memory
- 분류: survey
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Research in artificial intelligence is shifting from model innovations and benchmark scores towards problem definition and rigorous real-world evaluation. As the field enters the "second half," the central challenge becomes real utility in long-horizon, dynamic, and user-dependent settings such as agentic coding, deep research, and computer use, where LLM-based agents face context explosion beyond fixed context windows and must continuously accumulate, manage, and selectively reuse information across extended interactions. Memory, with hundreds of papers released in 2025, therefore emerges as the critical solution to fill this utility gap. Beyond passive storage, memory is increasingly the substrate through which agents self-evolve: short-term memory gates which experiences are perceived and abstracted during execution, while long-term memory consolidates them into reusable knowledge and skills, forming the loop through which agents improve from their own experience. In this survey, we provide a unified view of foundation agent memory along three dimensions: memory substrate (internal parametric state and external retrieval-augmented stores), cognitive mechanism (sensory, working, episodic, semantic, and procedural), and memory subject (user-centric personalization and agent-centric experience). We then analyze how memory is operated under single- and multi-agent topologies and highlight learning policies over memory operations, showing how memory management itself is becoming a trainable capability spanning reinforcement-learned context curation, experience consolidation at decision time, and the emerging ecosystem of portable, shareable agent skills. Finally, we review evaluation benchmarks and metrics for memory utility, and outline open challenges and future directions.

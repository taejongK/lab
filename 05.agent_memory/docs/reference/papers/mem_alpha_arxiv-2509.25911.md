# Mem-α: Learning Memory Construction via Reinforcement Learning

- 저자: Yu Wang, Ryuichi Takanobu, Zhiqi Liang, Yuzhen Mao et al.
- 날짜: 2025-09-30 (arXiv v1 제출일, 수집 버전 2509.25911v1)
- 학회/저널: arXiv preprint
- arXiv: https://arxiv.org/abs/2509.25911
- 코드: -
- 분류: training
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large language model (LLM) agents are constrained by limited context windows, necessitating external memory systems for long-term information understanding. Current memory-augmented agents typically depend on pre-defined instructions and tools for memory updates. However, language models may lack the ability to determine which information to store, how to structure it, and when to update it, especially as memory systems become more complex. This results in suboptimal memory construction and information loss. To this end, we propose Mem-alpha, a reinforcement learning framework that trains agents to effectively manage complex memory systems through interaction and feedback. We also construct a specialized training dataset spanning diverse multi-turn interaction patterns paired with comprehensive evaluation questions designed to teach effective memory management. During training, agents process sequential information chunks, learn to extract and store relevant content, then update the memory system. The reward signal derives from downstream question-answering accuracy over the full interaction history, directly optimizing for memory construction. To illustrate the effectiveness of our training framework, we design a memory architecture comprising core, episodic, and semantic components, equipped with multiple tools for memory operations. Empirical evaluation demonstrates that Mem-alpha achieves significant improvements over existing memory-augmented agent baselines. Despite being trained exclusively on instances with a maximum length of 30k tokens, our agents exhibit remarkable generalization to sequences exceeding 400k tokens, over 13x the training length, highlighting the robustness of Mem-alpha.

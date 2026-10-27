# Reflexion: Language Agents with Verbal Reinforcement Learning

- 저자: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath et al.
- 날짜: 2023-03-20 (arXiv v1 제출일, 수집 버전 2303.11366v4)
- 학회/저널: (arXiv comment) v4 contains a few additional experiments
- arXiv: https://arxiv.org/abs/2303.11366
- 코드: https://github.com/noahshinn/reflexion
- 분류: architecture
- 비고: pre-window (2023-03), foundational
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance.

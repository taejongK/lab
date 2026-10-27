# MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

- 저자: Shengtao Zhang, Jiaqian Wang, Ruiwen Zhou, Junwei Liao et al.
- 날짜: 2026-01-06 (arXiv v1 제출일, 수집 버전 2601.03192v2)
- 학회/저널: (arXiv comment) 41 pages, 11 figures
- arXiv: https://arxiv.org/abs/2601.03192
- 코드: https://github.com/MemTensor/MemRL
- 분류: training
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

The hallmark of human intelligence is the self-evolving ability to master new skills by learning from past experiences. However, current AI agents struggle to emulate this self-evolution: fine-tuning is computationally expensive and prone to catastrophic forgetting, while existing memory-based methods rely on passive semantic matching that often retrieves noise. To address these challenges, we propose MemRL, a non-parametric approach that evolves via reinforcement learning on episodic memory. By decoupling stable reasoning from plastic memory, MemRL employs a Two-Phase Retrieval mechanism to filter noise and identify high-utility strategies through environmental feedback. Extensive experiments on HLE, BigCodeBench, ALFWorld, and Lifelong Agent Bench demonstrate that MemRL significantly outperforms state-of-the-art baselines, confirming that MemRL effectively reconciles the stability-plasticity dilemma, enabling continuous runtime improvement without weight updates. Code is available at https://github.com/MemTensor/MemRL.

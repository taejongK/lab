# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

- 저자: Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan et al. (Wuhan University, Alibaba Group)
- 날짜: 2026-01-05 (arXiv v1 제출일, 수집 버전 2601.01885v3, 2026-07-23)
- 학회/저널: ACL 2026 (SAC Highlight, arXiv 코멘트 기준)
- arXiv: https://arxiv.org/abs/2601.01885
- 코드: https://github.com/y1y5/AgeMem
- 분류: training
- 수집일: 2026-11-14
- 출처: arxiv.org/abs 페이지, 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relying on heuristics or auxiliary controllers, which limits adaptability and end-to-end optimization. In this paper, we propose Agentic Memory (AgeMem), a unified framework that integrates LTM and STM management directly into the agent's policy. AgeMem exposes memory operations as tool-based actions, enabling the LLM agent to autonomously decide what and when to store, retrieve, update, summarize, or discard information. To train such unified behaviors, we propose a three-stage progressive reinforcement learning strategy and design a step-wise GRPO to address sparse and discontinuous rewards induced by memory operations. Experiments on five long-horizon benchmarks demonstrate that AgeMem consistently outperforms strong memory-augmented baselines across multiple LLM backbones, achieving improved task performance, higher-quality long-term memory, and more efficient context usage.

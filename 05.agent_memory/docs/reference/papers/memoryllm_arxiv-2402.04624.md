# MEMORYLLM: Towards Self-Updatable Large Language Models

- 저자: Yu Wang, Yifan Gao, Xiusi Chen, Haoming Jiang et al.
- 날짜: 2024-02-07 (arXiv v1 제출일, 수집 버전 2402.04624v2)
- 학회/저널: (arXiv comment) 13 pages, 9 figures
- arXiv: https://arxiv.org/abs/2402.04624
- 코드: https://github.com/wangyu-ustc/MemoryLLM
- 분류: architecture
- 비고: parametric memory
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Existing Large Language Models (LLMs) usually remain static after deployment, which might make it hard to inject new knowledge into the model. We aim to build models containing a considerable portion of self-updatable parameters, enabling the model to integrate new knowledge effectively and efficiently. To this end, we introduce MEMORYLLM, a model that comprises a transformer and a fixed-size memory pool within the latent space of the transformer. MEMORYLLM can self-update with text knowledge and memorize the knowledge injected earlier. Our evaluations demonstrate the ability of MEMORYLLM to effectively incorporate new knowledge, as evidenced by its performance on model editing benchmarks. Meanwhile, the model exhibits long-term information retention capacity, which is validated through our custom-designed evaluations and long-context benchmarks. MEMORYLLM also shows operational integrity without any sign of performance degradation even after nearly a million memory updates. Our code and model are open-sourced at https://github.com/wangyu-ustc/MemoryLLM.

# M+: Extending MemoryLLM with Scalable Long-Term Memory

- 저자: Yu Wang, Dmitry Krotov, Yuanzhe Hu, Yifan Gao et al.
- 날짜: 2025-02-01 (arXiv v1 제출일, 수집 버전 2502.00592v2)
- 학회/저널: arXiv preprint
- arXiv: https://arxiv.org/abs/2502.00592
- 코드: https://github.com/wangyu-ustc/MemoryLLM
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Equipping large language models (LLMs) with latent-space memory has attracted increasing attention as they can extend the context window of existing language models. However, retaining information from the distant past remains a challenge. For example, MemoryLLM (Wang et al., 2024a), as a representative work with latent-space memory, compresses past information into hidden states across all layers, forming a memory pool of 1B parameters. While effective for sequence lengths up to 16k tokens, it struggles to retain knowledge beyond 20k tokens. In this work, we address this limitation by introducing M+, a memory-augmented model based on MemoryLLM that significantly enhances long-term information retention. M+ integrates a long-term memory mechanism with a co-trained retriever, dynamically retrieving relevant information during text generation. We evaluate M+ on diverse benchmarks, including long-context understanding and knowledge retention tasks. Experimental results show that M+ significantly outperforms MemoryLLM and recent strong baselines, extending knowledge retention from under 20k to over 160k tokens with similar GPU memory overhead. We open-source our code at https://github.com/wangyu-ustc/MemoryLLM

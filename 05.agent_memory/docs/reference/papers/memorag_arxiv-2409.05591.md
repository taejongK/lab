# MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation

- 저자: Hongjin Qian, Zheng Liu, Peitian Zhang, Kelong Mao et al.
- 날짜: 2024-09-09 (arXiv v1 제출일, 수집 버전 2409.05591v3)
- 학회/저널: (arXiv comment) theWebConf 2025. Codes and models are in https://github.com/qhjqhj00/MemoRAG
- arXiv: https://arxiv.org/abs/2409.05591
- 코드: https://github.com/qhjqhj00/MemoRAG
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Processing long contexts presents a significant challenge for large language models (LLMs). While recent advancements allow LLMs to handle much longer contexts than before (e.g., 32K or 128K tokens), it is computationally expensive and can still be insufficient for many applications. Retrieval-Augmented Generation (RAG) is considered a promising strategy to address this problem. However, conventional RAG methods face inherent limitations because of two underlying requirements: 1) explicitly stated queries, and 2) well-structured knowledge. These conditions, however, do not hold in general long-context processing tasks. In this work, we propose MemoRAG, a novel RAG framework empowered by global memory-augmented retrieval. MemoRAG features a dual-system architecture. First, it employs a light but long-range system to create a global memory of the long context. Once a task is presented, it generates draft answers, providing useful clues for the retrieval tools to locate relevant information within the long context. Second, it leverages an expensive but expressive system, which generates the final answer based on the retrieved information. Building upon this fundamental framework, we realize the memory module in the form of KV compression, and reinforce its memorization and cluing capacity from the Generation quality's Feedback (a.k.a. RLGF). In our experiments, MemoRAG achieves superior performances across a variety of long-context evaluation tasks, not only complex scenarios where traditional RAG methods struggle, but also simpler ones where RAG is typically applied.

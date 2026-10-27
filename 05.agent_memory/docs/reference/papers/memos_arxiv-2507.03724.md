# MemOS: A Memory OS for AI System

- 저자: Zhiyu Li, Chenyang Xi, Chunyu Li, Ding Chen et al.
- 날짜: 2025-07-04 (arXiv v1 제출일, 수집 버전 2507.03724v4)
- 학회/저널: (arXiv comment) 36 pages, 10 figures, 5 tables
- arXiv: https://arxiv.org/abs/2507.03724
- 코드: https://github.com/MemTensor/MemOS
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large Language Models (LLMs) have become an essential infrastructure for Artificial General Intelligence (AGI), yet their lack of well-defined memory management systems hinders the development of long-context reasoning, continual personalization, and knowledge consistency.Existing models mainly rely on static parameters and short-lived contextual states, limiting their ability to track user preferences or update knowledge over extended periods.While Retrieval-Augmented Generation (RAG) introduces external knowledge in plain text, it remains a stateless workaround without lifecycle control or integration with persistent representations.Recent work has modeled the training and inference cost of LLMs from a memory hierarchy perspective, showing that introducing an explicit memory layer between parameter memory and external retrieval can substantially reduce these costs by externalizing specific knowledge. Beyond computational efficiency, LLMs face broader challenges arising from how information is distributed over time and context, requiring systems capable of managing heterogeneous knowledge spanning different temporal scales and sources. To address this challenge, we propose MemOS, a memory operating system that treats memory as a manageable system resource. It unifies the representation, scheduling, and evolution of plaintext, activation-based, and parameter-level memories, enabling cost-efficient storage and retrieval. As the basic unit, a MemCube encapsulates both memory content and metadata such as provenance and versioning. MemCubes can be composed, migrated, and fused over time, enabling flexible transitions between memory types and bridging retrieval with parameter-based learning. MemOS establishes a memory-centric system framework that brings controllability, plasticity, and evolvability to LLMs, laying the foundation for continual learning and personalized modeling.

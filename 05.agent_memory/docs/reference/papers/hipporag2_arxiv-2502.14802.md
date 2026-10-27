# From RAG to Memory: Non-Parametric Continual Learning for Large Language Models

- 저자: Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou et al.
- 날짜: 2025-02-20 (arXiv v1 제출일, 수집 버전 2502.14802v2)
- 학회/저널: (arXiv comment) ICML 2025. Code and data are available at: https://github.com/OSU-NLP-Group/HippoRAG
- arXiv: https://arxiv.org/abs/2502.14802
- 코드: https://github.com/OSU-NLP-Group/HippoRAG
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Our ability to continuously acquire, organize, and leverage knowledge is a key feature of human intelligence that AI systems must approximate to unlock their full potential. Given the challenges in continual learning with large language models (LLMs), retrieval-augmented generation (RAG) has become the dominant way to introduce new information. However, its reliance on vector retrieval hinders its ability to mimic the dynamic and interconnected nature of human long-term memory. Recent RAG approaches augment vector embeddings with various structures like knowledge graphs to address some of these gaps, namely sense-making and associativity. However, their performance on more basic factual memory tasks drops considerably below standard RAG. We address this unintended deterioration and propose HippoRAG 2, a framework that outperforms standard RAG comprehensively on factual, sense-making, and associative memory tasks. HippoRAG 2 builds upon the Personalized PageRank algorithm used in HippoRAG and enhances it with deeper passage integration and more effective online use of an LLM. This combination pushes this RAG system closer to the effectiveness of human long-term memory, achieving a 7% improvement in associative memory tasks over the state-of-the-art embedding model while also exhibiting superior factual knowledge and sense-making memory capabilities. This work paves the way for non-parametric continual learning for LLMs. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

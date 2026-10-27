# ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory

- 저자: Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo et al.
- 날짜: 2023-06-06 (arXiv v1 제출일, 수집 버전 2306.03901v2)
- 학회/저널: arXiv preprint
- arXiv: https://arxiv.org/abs/2306.03901
- 코드: -
- 분류: architecture
- 비고: pre-window (2023-06)
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large language models (LLMs) with memory are computationally universal. However, mainstream LLMs are not taking full advantage of memory, and the designs are heavily influenced by biological brains. Due to their approximate nature and proneness to the accumulation of errors, conventional neural memory mechanisms cannot support LLMs to simulate complex reasoning. In this paper, we seek inspiration from modern computer architectures to augment LLMs with symbolic memory for complex multi-hop reasoning. Such a symbolic memory framework is instantiated as an LLM and a set of SQL databases, where the LLM generates SQL instructions to manipulate the SQL databases. We validate the effectiveness of the proposed memory framework on a synthetic dataset requiring complex reasoning. The project website is available at https://chatdatabase.github.io/ .

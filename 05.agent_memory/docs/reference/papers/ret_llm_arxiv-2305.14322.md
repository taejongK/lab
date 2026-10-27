# RET-LLM: Towards a General Read-Write Memory for Large Language Models

- 저자: Ali Modarressi, Ayyoob Imani, Mohsen Fayyaz, Hinrich Schütze
- 날짜: 2023-05-23 (arXiv v1 제출일, 수집 버전 2305.14322v2)
- 학회/저널: (arXiv comment) NOTE: This concept paper outlines an initial methodology, now evolved and thoroughly evaluated in the MemLLM paper
- arXiv: https://arxiv.org/abs/2305.14322
- 코드: -
- 분류: architecture
- 비고: pre-window (2023-05)
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large language models (LLMs) have significantly advanced the field of natural language processing (NLP) through their extensive parameters and comprehensive data utilization. However, existing LLMs lack a dedicated memory unit, limiting their ability to explicitly store and retrieve knowledge for various tasks. In this paper, we propose RET-LLM a novel framework that equips LLMs with a general write-read memory unit, allowing them to extract, store, and recall knowledge from the text as needed for task performance. Inspired by Davidsonian semantics theory, we extract and save knowledge in the form of triplets. The memory unit is designed to be scalable, aggregatable, updatable, and interpretable. Through qualitative evaluations, we demonstrate the superiority of our proposed framework over baseline approaches in question answering tasks. Moreover, our framework exhibits robust performance in handling temporal-based question answering tasks, showcasing its ability to effectively manage time-dependent information.

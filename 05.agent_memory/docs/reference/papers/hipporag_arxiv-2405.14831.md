# HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

- 저자: Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga et al.
- 날짜: 2024-05-23 (arXiv v1 제출일, 수집 버전 2405.14831v3)
- 학회/저널: (arXiv comment) NeurIPS 2024. Code and data: https://github.com/OSU-NLP-Group/HippoRAG
- arXiv: https://arxiv.org/abs/2405.14831
- 코드: https://github.com/OSU-NLP-Group/HippoRAG
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

In order to thrive in hostile and ever-changing natural environments, mammalian brains evolved to store large amounts of knowledge about the world and continually integrate new information while avoiding catastrophic forgetting. Despite the impressive accomplishments, large language models (LLMs), even with retrieval-augmented generation (RAG), still struggle to efficiently and effectively integrate a large amount of new experiences after pre-training. In this work, we introduce HippoRAG, a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory to enable deeper and more efficient knowledge integration over new experiences. HippoRAG synergistically orchestrates LLMs, knowledge graphs, and the Personalized PageRank algorithm to mimic the different roles of neocortex and hippocampus in human memory. We compare HippoRAG with existing RAG methods on multi-hop question answering and show that our method outperforms the state-of-the-art methods remarkably, by up to 20%. Single-step retrieval with HippoRAG achieves comparable or better performance than iterative retrieval like IRCoT while being 10-30 times cheaper and 6-13 times faster, and integrating HippoRAG into IRCoT brings further substantial gains. Finally, we show that our method can tackle new types of scenarios that are out of reach of existing methods. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

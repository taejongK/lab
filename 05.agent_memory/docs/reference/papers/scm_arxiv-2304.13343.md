# SCM: Enhancing Large Language Model with Self-Controlled Memory Framework

- 저자: Bing Wang, Xinnian Liang, Jian Yang, Hui Huang et al.
- 날짜: 2023-04-26 (arXiv v1 제출일, 수집 버전 2304.13343v4)
- 학회/저널: (arXiv comment) Accepted by DASFAA 2025 main conference
- arXiv: https://arxiv.org/abs/2304.13343
- 코드: https://github.com/wbbeyourself/SCM4LLMs
- 분류: architecture
- 비고: pre-window (2023-04)
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Large Language Models (LLMs) are constrained by their inability to process lengthy inputs, resulting in the loss of critical historical information. To address this limitation, in this paper, we propose the Self-Controlled Memory (SCM) framework to enhance the ability of LLMs to maintain long-term memory and recall relevant information. Our SCM framework comprises three key components: an LLM-based agent serving as the backbone of the framework, a memory stream storing agent memories, and a memory controller updating memories and determining when and how to utilize memories from memory stream. Additionally, the proposed SCM is able to process ultra-long texts without any modification or fine-tuning, which can integrate with any instruction following LLMs in a plug-and-play paradigm. Furthermore, we annotate a dataset to evaluate the effectiveness of SCM for handling lengthy inputs. The annotated dataset covers three tasks: long-term dialogues, book summarization, and meeting summarization. Experimental results demonstrate that our method achieves better retrieval recall and generates more informative responses compared to competitive baselines in long-term dialogues. (https://github.com/wbbeyourself/SCM4LLMs)

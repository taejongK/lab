# LightMem: Lightweight and Efficient Memory-Augmented Generation

- 저자: Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang et al.
- 날짜: 2025-10-21 (arXiv v1 제출일, 수집 버전 2510.18866v4)
- 학회/저널: (arXiv comment) ICLR 2026
- arXiv: https://arxiv.org/abs/2510.18866
- 코드: https://github.com/zjunlp/LightMem
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Despite their remarkable capabilities, Large Language Models (LLMs) struggle to effectively leverage historical interaction information in dynamic and complex environments. Memory systems enable LLMs to move beyond stateless interactions by introducing persistent information storage, retrieval, and utilization mechanisms. However, existing memory systems often introduce substantial time and computational overhead. To this end, we introduce a new memory system called LightMem, which strikes a balance between the performance and efficiency of memory systems. Inspired by the Atkinson-Shiffrin model of human memory, LightMem organizes memory into three complementary stages. First, cognition-inspired sensory memory rapidly filters irrelevant information through lightweight compression and groups information according to their topics. Next, topic-aware short-term memory consolidates these topic-based groups, organizing and summarizing content for more structured access. Finally, long-term memory with sleep-time update employs an offline procedure that decouples consolidation from online inference. On LongMemEval and LoCoMo, using GPT and Qwen backbones, LightMem consistently surpasses strong baselines, improving QA accuracy by up to 7.7% / 29.3%, reducing total token usage by up to 38x / 20.9x and API calls by up to 30x / 55.5x, while purely online test-time costs are even lower, achieving up to 106x / 117x token reduction and 159x / 310x fewer API calls. The code is available at https://github.com/zjunlp/LightMem.

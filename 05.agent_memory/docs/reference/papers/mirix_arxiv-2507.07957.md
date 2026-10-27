# MIRIX: Multi-Agent Memory System for LLM-Based Agents

- 저자: Yu Wang, Xi Chen
- 날짜: 2025-07-10 (arXiv v1 제출일, 수집 버전 2507.07957v1)
- 학회/저널: arXiv preprint
- arXiv: https://arxiv.org/abs/2507.07957
- 코드: -
- 분류: architecture
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Although memory capabilities of AI agents are gaining increasing attention, existing solutions remain fundamentally limited. Most rely on flat, narrowly scoped memory components, constraining their ability to personalize, abstract, and reliably recall user-specific information over time. To this end, we introduce MIRIX, a modular, multi-agent memory system that redefines the future of AI memory by solving the field's most critical challenge: enabling language models to truly remember. Unlike prior approaches, MIRIX transcends text to embrace rich visual and multimodal experiences, making memory genuinely useful in real-world scenarios. MIRIX consists of six distinct, carefully structured memory types: Core, Episodic, Semantic, Procedural, Resource Memory, and Knowledge Vault, coupled with a multi-agent framework that dynamically controls and coordinates updates and retrieval. This design enables agents to persist, reason over, and accurately retrieve diverse, long-term user data at scale. We validate MIRIX in two demanding settings. First, on ScreenshotVQA, a challenging multimodal benchmark comprising nearly 20,000 high-resolution computer screenshots per sequence, requiring deep contextual understanding and where no existing memory systems can be applied, MIRIX achieves 35% higher accuracy than the RAG baseline while reducing storage requirements by 99.9%. Second, on LOCOMO, a long-form conversation benchmark with single-modal textual input, MIRIX attains state-of-the-art performance of 85.4%, far surpassing existing baselines. These results show that MIRIX sets a new performance standard for memory-augmented LLM agents. To allow users to experience our memory system, we provide a packaged application powered by MIRIX. It monitors the screen in real time, builds a personalized memory base, and offers intuitive visualization and secure local storage to ensure privacy.

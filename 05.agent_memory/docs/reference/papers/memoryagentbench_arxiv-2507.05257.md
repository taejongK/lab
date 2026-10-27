# Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions

- 저자: Yuanzhe Hu, Yu Wang, Julian McAuley
- 날짜: 2025-07-07 (arXiv v1 제출일, 수집 버전 2507.05257v4)
- 학회/저널: (arXiv comment) Y. Hu and Y. Wang contribute equally
- arXiv: https://arxiv.org/abs/2507.05257
- 코드: -
- 분류: benchmark
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Recent benchmarks for Large Language Model (LLM) agents primarily focus on evaluating reasoning, planning, and execution capabilities, while another critical component-memory, encompassing how agents memorize, update, and retrieve long-term information-is under-evaluated due to the lack of benchmarks. We term agents with memory mechanisms as memory agents. In this paper, based on classic theories from memory science and cognitive science, we identify four core competencies essential for memory agents: accurate retrieval, test-time learning, long-range understanding, and selective forgetting. Existing benchmarks either rely on limited context lengths or are tailored for static, long-context settings like book-based QA, which do not reflect the interactive, multi-turn nature of memory agents that incrementally accumulate information. Moreover, no existing benchmarks cover all four competencies. We introduce MemoryAgentBench, a new benchmark specifically designed for memory agents. Our benchmark transforms existing long-context datasets and incorporates newly constructed datasets into a multi-turn format, effectively simulating the incremental information processing characteristic of memory agents. By carefully selecting and curating datasets, our benchmark provides comprehensive coverage of the four core memory competencies outlined above, thereby offering a systematic and challenging testbed for assessing memory quality. We evaluate a diverse set of memory agents, ranging from simple context-based and retrieval-augmented generation (RAG) systems to advanced agents with external memory modules and tool integration. Empirical results reveal that current methods fall short of mastering all four competencies, underscoring the need for further research into comprehensive memory mechanisms for LLM agents.

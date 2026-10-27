# MemoryBank: Enhancing Large Language Models with Long-Term Memory

- 저자: Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye et al.
- 날짜: 2023-05-17 (arXiv v1 제출일, 수집 버전 2305.10250v3)
- 학회/저널: (arXiv comment) 10 pages
- arXiv: https://arxiv.org/abs/2305.10250
- 코드: -
- 분류: architecture
- 비고: pre-window (2023-05)
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

Revolutionary advancements in Large Language Models have drastically reshaped our interactions with artificial intelligence systems. Despite this, a notable hindrance remains-the deficiency of a long-term memory mechanism within these models. This shortfall becomes increasingly evident in situations demanding sustained interaction, such as personal companion systems and psychological counseling. Therefore, we propose MemoryBank, a novel memory mechanism tailored for LLMs. MemoryBank enables the models to summon relevant memories, continually evolve through continuous memory updates, comprehend, and adapt to a user personality by synthesizing information from past interactions. To mimic anthropomorphic behaviors and selectively preserve memory, MemoryBank incorporates a memory updating mechanism, inspired by the Ebbinghaus Forgetting Curve theory, which permits the AI to forget and reinforce memory based on time elapsed and the relative significance of the memory, thereby offering a human-like memory mechanism. MemoryBank is versatile in accommodating both closed-source models like ChatGPT and open-source models like ChatGLM. We exemplify application of MemoryBank through the creation of an LLM-based chatbot named SiliconFriend in a long-term AI Companion scenario. Further tuned with psychological dialogs, SiliconFriend displays heightened empathy in its interactions. Experiment involves both qualitative analysis with real-world user dialogs and quantitative analysis with simulated dialogs. In the latter, ChatGPT acts as users with diverse characteristics and generates long-term dialog contexts covering a wide array of topics. The results of our analysis reveal that SiliconFriend, equipped with MemoryBank, exhibits a strong capability for long-term companionship as it can provide emphatic response, recall relevant memories and understand user personality.

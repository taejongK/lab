# Voyager: An Open-Ended Embodied Agent with Large Language Models

- 저자: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar et al.
- 날짜: 2023-05-25 (arXiv v1 제출일, 수집 버전 2305.16291v2)
- 학회/저널: (arXiv comment) Project website and open-source codebase: https://voyager.minedojo.org/
- arXiv: https://arxiv.org/abs/2305.16291
- 코드: https://github.com/MineDojo/Voyager
- 분류: architecture
- 비고: pre-window (2023-05), skill library
- 수집일: 2026-10-27
- 출처: arXiv API (export.arxiv.org), 초록 원문 그대로 (줄바꿈만 정리)

## Abstract

We introduce Voyager, the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention. Voyager consists of three key components: 1) an automatic curriculum that maximizes exploration, 2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and 3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement. Voyager interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning. The skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting. Empirically, Voyager shows strong in-context lifelong learning capability and exhibits exceptional proficiency in playing Minecraft. It obtains 3.3x more unique items, travels 2.3x longer distances, and unlocks key tech tree milestones up to 15.3x faster than prior SOTA. Voyager is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch, while other techniques struggle to generalize. We open-source our full codebase and prompts at https://voyager.minedojo.org/.

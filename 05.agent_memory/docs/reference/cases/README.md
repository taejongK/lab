# Cases — 실제 에이전트 메모리 구현 사례 원문

제품·오픈소스·엔지니어링 글 원문 모음 (2023-10 ~ 2026-10). 수집일 2026-10-27.
요약이 아니라 원문 저장본이다. 각 파일 상단에 URL·발행일·수집 방식을 적어 두었다.

## 1. 상용 어시스턴트 메모리

| 자료 | 출처 | 날짜 | 링크 | 파일 |
|---|---|---|---|---|
| Memory and new controls for ChatGPT | OpenAI | 2024-02-13 (갱신 2025-04-10, 2025-06-03) | [link](https://openai.com/index/memory-and-new-controls-for-chatgpt/) | [chatgpt-memory_openai-blog.md](chatgpt-memory_openai-blog.md) |
| Memory FAQ | OpenAI Help Center | 상시 갱신 (날짜 미표기) | [link](https://help.openai.com/en/articles/8590148-memory-faq) | [chatgpt-memory_openai-help-faq.md](chatgpt-memory_openai-help-faq.md) |
| Bringing memory to Claude | Anthropic | 2025-09-11 (갱신 2025-10-23) | [link](https://www.anthropic.com/news/memory) | [claude-memory_anthropic-news.md](claude-memory_anthropic-news.md) |
| Managing context on the Claude Developer Platform (context editing + memory tool) | Anthropic | 2025-09-29 | [link](https://www.anthropic.com/news/context-management) | [claude-context-management_anthropic-news.md](claude-context-management_anthropic-news.md) |
| Memory tool | Anthropic (Claude Platform Docs) | 상시 갱신 | [link](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) | [claude-memory-tool_anthropic-docs.md](claude-memory-tool_anthropic-docs.md) |
| Gemini adds Temporary Chats and new personalization features | Google (The Keyword) | 2025-08-13 | [link](https://blog.google/products/gemini/temporary-chats-privacy-controls/) | [gemini-personal-context_google-blog.md](gemini-personal-context_google-blog.md) |
| Save info and reference past chats in Gemini Apps | Google Gemini Help | 상시 갱신 | [link](https://support.google.com/gemini/answer/16413516) | [gemini-memory_google-help.md](gemini-memory_google-help.md) |
| Introducing Copilot Memory: A More Productive and Personalized AI for the Way You Work | Microsoft Tech Community (Microsoft 365 Copilot Blog) | 2025-07-14 | [link](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-copilot-memory-a-more-productive-and-personalized-ai-for-the-way-you-work/4432059) | [m365-copilot-memory_microsoft-techcommunity.md](m365-copilot-memory_microsoft-techcommunity.md) |

## 2. 코딩 에이전트 메모리

| 자료 | 출처 | 날짜 | 링크 | 파일 |
|---|---|---|---|---|
| How Claude remembers your project (CLAUDE.md / auto memory) | Anthropic (Claude Code Docs) | 상시 갱신 | [link](https://code.claude.com/docs/en/memory) | [claude-code-memory_anthropic-docs.md](claude-code-memory_anthropic-docs.md) |
| Rules | Cursor Docs | 상시 갱신 | [link](https://cursor.com/docs/context/rules) | [cursor-rules_cursor-docs.md](cursor-rules_cursor-docs.md) |
| Cascade Memories (Windsurf) | Cognition (docs.devin.ai) | 상시 갱신 | [link](https://docs.devin.ai/windsurf/plugins/cascade/memories) | [windsurf-memories_devin-docs.md](windsurf-memories_devin-docs.md) |
| Building an agentic memory system for GitHub Copilot | GitHub Blog (Tiferet Gazit) | 2026-01-15 | [link](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) | [copilot-agentic-memory_github-blog.md](copilot-agentic-memory_github-blog.md) |
| About Copilot Memory | GitHub Docs | 상시 갱신 | [link](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-memory) | [copilot-memory_github-docs.md](copilot-memory_github-docs.md) |
| AGENTS.md — A simple, open format for guiding coding agents | agents.md | 상시 갱신 | [link](https://agents.md/) | [agents-md_agents-md-site.md](agents-md_agents-md-site.md) |
| Custom instructions with AGENTS.md (Codex) | OpenAI Developers | 상시 갱신 | [link](https://developers.openai.com/codex/guides/agents-md) | [codex-agents-md_openai-docs.md](codex-agents-md_openai-docs.md) |

## 3. 오픈소스 메모리 프레임워크/서비스

| 자료 | 출처 | 날짜 | 링크 | 파일 |
|---|---|---|---|---|
| letta-ai/letta README (MemGPT 후신, 현재는 letta-code로 이전 안내) | Letta | 확인일 기준 main | [link](https://github.com/letta-ai/letta) | [letta_github-readme.md](letta_github-readme.md) |
| Memory | Letta Docs (memory blocks, MemFS, dreaming) | Letta Docs | 상시 갱신 | [link](https://docs.letta.com/agent-sdk/memory/) | [letta-memory_letta-docs.md](letta-memory_letta-docs.md) |
| MemFS | Letta Docs (git-versioned memory filesystem) | Letta Docs | 상시 갱신 | [link](https://docs.letta.com/concepts/memfs/) | [letta-memfs_letta-docs.md](letta-memfs_letta-docs.md) |
| mem0ai/mem0 README | Mem0 | 확인일 기준 main | [link](https://github.com/mem0ai/mem0) | [mem0_github-readme.md](mem0_github-readme.md) |
| getzep/graphiti README (Zep 시간 지식그래프) | Zep | 확인일 기준 main | [link](https://github.com/getzep/graphiti) | [graphiti_github-readme.md](graphiti_github-readme.md) |
| langchain-ai/langmem README | LangChain | 확인일 기준 main | [link](https://github.com/langchain-ai/langmem) | [langmem_github-readme.md](langmem_github-readme.md) |
| Memory overview (LangGraph: short-term / long-term, semantic·episodic·procedural) | LangChain Docs | 상시 갱신 | [link](https://docs.langchain.com/oss/python/concepts/memory) | [langgraph-memory_langchain-docs.md](langgraph-memory_langchain-docs.md) |
| Memory (LlamaIndex agents) | LlamaIndex Docs | 상시 갱신 | [link](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/memory/) | [llamaindex-memory_llamaindex-docs.md](llamaindex-memory_llamaindex-docs.md) |
| topoteretes/cognee README | cognee | 확인일 기준 main | [link](https://github.com/topoteretes/cognee) | [cognee_github-readme.md](cognee_github-readme.md) |
| memodb-io/memobase README | Memobase | 확인일 기준 main | [link](https://github.com/memodb-io/memobase) | [memobase_github-readme.md](memobase_github-readme.md) |
| MemTensor/MemOS README | MemTensor | 확인일 기준 main | [link](https://github.com/MemTensor/MemOS) | [memos_github-readme.md](memos_github-readme.md) |
| supermemoryai/supermemory README | Supermemory | 확인일 기준 main | [link](https://github.com/supermemoryai/supermemory) | [supermemory_github-readme.md](supermemory_github-readme.md) |
| Memory (CrewAI unified memory) | CrewAI Docs | 상시 갱신 | [link](https://docs.crewai.com/en/concepts/memory) | [crewai-memory_crewai-docs.md](crewai-memory_crewai-docs.md) |
| Memory and RAG (AutoGen AgentChat) | Microsoft AutoGen Docs | 상시 갱신 (stable) | [link](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html) | [autogen-memory_microsoft-docs.md](autogen-memory_microsoft-docs.md) |

## 4. 엔지니어링 글 (프로덕션 구축기)

| 자료 | 출처 | 날짜 | 링크 | 파일 |
|---|---|---|---|---|
| Memory for agents | LangChain Blog (Harrison Chase) | 2024-10-19 | [link](https://blog.langchain.com/memory-for-agents/) | [memory-for-agents_langchain-blog.md](memory-for-agents_langchain-blog.md) |
| Sleep-time Compute | Letta Blog | 2025-04-21 | [link](https://www.letta.com/blog/sleep-time-compute) | [letta-sleep-time-compute_letta-blog.md](letta-sleep-time-compute_letta-blog.md) |
| Context Engineering for AI Agents: Lessons from Building Manus | Manus (Yichao 'Peak' Ji) | 2025-07-18 | [link](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) | [manus-context-engineering_manus-blog.md](manus-context-engineering_manus-blog.md) |
| Effective context engineering for AI agents | Anthropic Engineering | 2025-09-29 | [link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [context-engineering_anthropic-engineering.md](context-engineering_anthropic-engineering.md) |
| How we built our multi-agent research system | Anthropic Engineering | 2025-06-13 | [link](https://www.anthropic.com/engineering/multi-agent-research-system) | [multi-agent-research_anthropic-engineering.md](multi-agent-research_anthropic-engineering.md) |

## 수집 실패·제외

- Memobase: `main/README.md` 404 → 실제 파일명 `readme.md`로 재수집 (성공)
- Zep 블로그 (blog.getzep.com/zep-a-temporal-knowledge-graph-architecture-for-agent-memory/): 본문 추출 1.9k자로 불완전해 제외. Graphiti README로 대체
- Microsoft 소비자용 Copilot 메모리 (2025-04 발표): 공식 원문 URL 못 찾음, 2차 기사만 존재 → 제외

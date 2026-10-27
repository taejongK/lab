# AGENTS.md — A simple, open format for guiding coding agents

- 제목: AGENTS.md — A simple, open format for guiding coding agents
- 발행: agents.md
- 발행일: 상시 갱신
- URL: https://agents.md/
- 수집일: 2026-10-27
- 그룹: 2. 코딩 에이전트 메모리
- 유형: docs
- 수집 방식: HTML 본문 추출 (trafilatura, 내비게이션·푸터 제거). 요약하지 않은 원문. 이미지·일부 서식은 빠졌을 수 있음.

---

# AGENTS.md

A simple, open format for guiding coding agents, 

used by over [60k open-source projects](https://github.com/search?q=path%3AAGENTS.md+NOT+is%3Afork+NOT+is%3Aarchived&type=code).

Think of AGENTS.md as a **README for agents**: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project.

``# AGENTS.md ## Setup commands- Install deps: `pnpm install`- Start dev server: `pnpm dev`- Run tests: `pnpm test` ## Code style- TypeScript strict mode- Single quotes, no semicolons- Use functional patterns where possible``
## Why AGENTS.md?

README.md files are for humans: quick starts, project descriptions, and contribution guidelines.

AGENTS.md complements this by containing the extra, sometimes detailed context coding agents need: build steps, tests, and conventions that might clutter a README or aren’t relevant to human contributors.

We intentionally kept it separate to:

Give agents a clear, predictable place for instructions.

Keep READMEs concise and focused on human contributors.

Provide precise, agent-focused guidance that complements existing README and docs.

Rather than introducing another proprietary file, we chose a name and format that could work for anyone. If you’re building or using coding agents and find this helpful, feel free to adopt it.

## One AGENTS.md works across many agents

Your agent definitions are compatible with a growing ecosystem of AI coding agents and tools:

## Examples

``# Sample AGENTS.md file ## Dev environment tips- Use `pnpm dlx turbo run where <project_name>` to jump to a package instead of scanning with `ls`.- Run `pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.- Use `pnpm create vite@latest <project_name> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.- Check the name field inside each package's package.json to confirm the right name—skip the top-level one. ## Testing instructions- Find the CI plan in the .github/workflows folder.- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.- Fix any test or type errors until the whole suite is green.- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.- Add or update tests for the code you change, even if nobody asked. ## PR instructions- Title format: [<project_name>] <Title>- Always run `pnpm lint` and `pnpm test` before committing.``
## How to use AGENTS.md?

### 1. Add AGENTS.md

### 2. Cover what matters

Add sections that help an agent work effectively with your project. Popular choices:

- Project overview
- Build and test commands
- Code style guidelines
- Testing instructions
- Security considerations

### 3. Add extra instructions

### 4. Large monorepo? Use nested AGENTS.md files for subprojects

## About

AGENTS.md emerged from collaborative efforts across the AI software development ecosystem, including [OpenAI Codex](https://openai.com/codex/), [Amp](https://ampcode.com), [Jules from Google](https://jules.google), [Cursor](https://cursor.com), and [Factory](https://factory.ai).

We’re committed to helping maintain and evolve this as an open format that benefits the entire developer community, regardless of which coding agent you use.

AGENTS.md is now stewarded by the [Agentic AI Foundation](https://aaif.io) under the Linux Foundation. [Learn more →](https://openai.com/index/agentic-ai-foundation/)

## FAQ

### Are there required fields?

### What if instructions conflict?

### Will the agent run testing commands found in AGENTS.md automatically?

### Can I update it later?

### How do I migrate existing docs to AGENTS.md?

Rename existing files to AGENTS.md and create symbolic links for backward compatibility:

`mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`
### How do I configure Aider?

Configure Aider to use AGENTS.md in `.aider.conf.yml`:

`read: AGENTS.md`
### How do I configure Gemini CLI?

Configure Gemini CLI to use AGENTS.md in `.gemini/settings.json`:

`{ "context": { "fileName": "AGENTS.md" }, }`

---
name: new-study
description: lab 저장소에 새 실험/스터디 폴더(NN.주제/)를 표준 포맷으로 만든다. research/poc를 먼저 묻고, README(시작일·최종 수정일)·AGENTS.md를 깐 뒤 /worklog-discipline:init-workstructure 로 docs 구조와 CLAUDE.md를 구성, 루트 README 표 갱신까지. "새 실험", "새 스터디", "새 프로젝트 폴더" 요청 시 사용.
---

# new-study

lab 저장소에 새 실험 폴더를 만든다. 템플릿은 이 스킬의 `template/` 폴더에 있다.

## 입력

- **모드**: `research` | `poc`. **폴더를 만들기 전에 반드시 사용자에게 묻는다** (AskUserQuestion). 요청에 이미 명시돼 있으면 묻지 않는다.
  - research: 실험·조사 중심 → `docs/report/`, `docs/reference/`
  - poc: 개발 계획 중심 → `docs/plan/active/`, `docs/plan/done/`, `docs/reference/`
- **주제**: 폴더명에 쓸 짧은 영문 kebab-case 슬러그 (예: `jev`, `rope-vs-alibi`). 한글 주제를 받으면 영문 슬러그로 바꿔 제안한다.
- **질문**: README의 "질문" 한 줄. 없으면 `(작성 예정)`으로 둔다.
- **제목**: README 첫 줄. 없으면 주제로 만든다.

## 절차

0. **모드 확인**: 위 입력의 모드를 아직 모르면 여기서 묻는다. 답을 받기 전에는 아무것도 만들지 않는다.
1. **번호 정하기**: 저장소 루트에서 `[0-9][0-9].*` 폴더 중 가장 큰 번호 + 1. 두 자리로 맞춘다.
   ```bash
   ls -d [0-9][0-9].*/ 2>/dev/null | sort | tail -1
   ```
2. **복사**: `cp -R .claude/skills/new-study/template/ NN.주제/` (README.md, AGENTS.md, docs/notes, docs/reference만 들어 있다)
3. **치환**: 아래 자리표시자를 채운다. 날짜는 오늘(`date +%F`).
   - `README.md`: `{제목}`, `{뭘 확인하려는가}`, 시작일·최종 수정일 `{YYYY-MM-DD}`
   - `AGENTS.md`: `{YYYY-MM-DD}`, `{NN.주제}`, Purpose 문장, 모드 폴더 행
     (research → `` `docs/report/` `` | 실험 결과·보고서, poc → `` `docs/plan/` `` | 개발 계획 (active/done))
4. **init-workstructure**: `cd NN.주제` 후 Skill `worklog-discipline:init-workstructure`를 args `"<모드> <git user.name>"`로 실행한다.
   현재 디렉터리 기준으로 docs/{worklog,report|plan,reference}, docs/index.md, CLAUDE.md(자동 문서화 규칙)를 만든다. AGENTS.md는 이미 있으므로 건너뛴다.
   끝나면 저장소 루트로 돌아온다.
5. **lab 확장 규칙**: `NN.주제/CLAUDE.md`의 `<!-- PROJECT-EXTENSIONS: ... -->` 줄 바로 아래에 `.claude/skills/new-study/claude-extension.md` 내용을 붙인다.
   `docs/index.md`에 `## notes` 섹션(직접 작성한 스터디 문서)을 추가한다.
6. **루트 README.md**: "프로젝트 목록" 표 맨 아래에 `| [NN.주제/](NN.주제/) | 진행중 | 한 줄 설명 |`을 추가한다.
7. **worklog**: `NN.주제/docs/worklog/{YYYY_MM_DD}.md`에 폴더 생성 기록(모드 포함)을 남긴다 (작업자는 git user.name).
8. **확인**: `find NN.주제 -type f | sort`로 구조를 보여주고, `grep -n '{' NN.주제/README.md NN.주제/AGENTS.md`로 자리표시자가 안 남았는지,
   `grep -c 'auto-doc-rules' NN.주제/CLAUDE.md`로 규칙 블록이 들어갔는지 확인한다.

## 만들어지는 구조

```
NN.주제/
├── README.md           # 질문·상태·시작일·최종 수정일·결론 + 문서 목록
├── CLAUDE.md           # init-workstructure 자동 문서화 규칙 + lab 확장(문서 위치)
├── AGENTS.md
└── docs/
    ├── index.md        # 문서 목차
    ├── notes/          # 직접 작성한 문서. NN.주제.md
    ├── reference/      # 외부 자료. README.md에 링크 표
    ├── worklog/        # YYYY_MM_DD.md
    └── report/         # research 모드
        또는 plan/{active,done}/   # poc 모드
```

## 이후 작업에서 지킬 것

- 직접 쓴 문서는 `docs/notes/NN.주제.md`로 번호를 붙이고, README 문서 표에 한 줄 추가한다.
- 외부 자료는 `docs/reference/`에 두고 `docs/reference/README.md` 표에 추가한다.
- 폴더 안의 파일을 바꾸면 README의 **최종 수정일**을 갱신한다.
- 상태가 바뀌면 프로젝트 README와 루트 README 표를 같이 갱신한다.

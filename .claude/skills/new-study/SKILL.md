---
name: new-study
description: lab 저장소에 새 실험/스터디 폴더(NN.주제/)를 표준 포맷으로 만든다. README(시작일·최종 수정일), CLAUDE.md, AGENTS.md, docs/{notes,reference,worklog,plan} 스캐폴드와 루트 README 표 갱신까지. "새 실험", "새 스터디", "새 프로젝트 폴더" 요청 시 사용.
---

# new-study

lab 저장소에 새 실험 폴더를 만든다. 템플릿은 이 스킬의 `template/` 폴더에 있다.

## 입력

- **주제**: 폴더명에 쓸 짧은 영문 kebab-case 슬러그 (예: `jev`, `rope-vs-alibi`). 한글 주제를 받으면 영문 슬러그로 바꿔 제안한다.
- **질문**: README의 "질문" 한 줄. 없으면 `(작성 예정)`으로 둔다.
- **제목**: README 첫 줄. 없으면 주제로 만든다.

## 절차

1. **번호 정하기**: 저장소 루트에서 `[0-9][0-9].*` 폴더 중 가장 큰 번호 + 1. 두 자리로 맞춘다.
   ```bash
   ls -d [0-9][0-9].*/ 2>/dev/null | sort | tail -1
   ```
2. **복사**: `cp -R .claude/skills/new-study/template/ NN.주제/`
3. **치환**: 아래 자리표시자를 채운다. 날짜는 오늘(`date +%F`).
   - `README.md`: `{제목}`, `{뭘 확인하려는가}`, 시작일·최종 수정일 `{YYYY-MM-DD}`
   - `AGENTS.md`: `{YYYY-MM-DD}`, `{NN.주제}`, Purpose 문장
   - `docs/plan/templates/` 안의 자리표시자는 **그대로 둔다** (템플릿이므로)
4. **루트 README.md**: "프로젝트 목록" 표 맨 아래에 `| [NN.주제/](NN.주제/) | 진행중 | 한 줄 설명 |`을 추가한다.
5. **worklog**: `NN.주제/docs/worklog/{YYYY_MM_DD}.md`에 폴더 생성 기록을 남긴다 (작업자는 git user.name).
6. **확인**: `find NN.주제 -type f | sort`로 구조를 보여주고, 자리표시자 `{`가 README/AGENTS에 남지 않았는지 `grep -n '{' NN.주제/README.md NN.주제/AGENTS.md`로 확인한다.

## 만들어지는 구조

```
NN.주제/
├── README.md           # 질문·상태·시작일·최종 수정일·결론 + 문서 목록
├── CLAUDE.md           # worklog-discipline 자동 문서화 규칙 + 문서 위치 규칙
├── AGENTS.md
└── docs/
    ├── notes/          # 직접 작성한 문서. NN.주제.md
    ├── reference/      # 외부 자료. README.md에 링크 표
    ├── worklog/        # YYYY_MM_DD.md
    └── plan/           # active/ completed/ templates/ handover-index.md
```

## 이후 작업에서 지킬 것

- 직접 쓴 문서는 `docs/notes/NN.주제.md`로 번호를 붙이고, README 문서 표에 한 줄 추가한다.
- 외부 자료는 `docs/reference/`에 두고 `docs/reference/README.md` 표에 추가한다.
- 폴더 안의 파일을 바꾸면 README의 **최종 수정일**을 갱신한다.
- 상태가 바뀌면 프로젝트 README와 루트 README 표를 같이 갱신한다.

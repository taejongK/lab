# lab

개인 실험용 모노레포. 논문 리뷰, 논문 구현, 아이디어 프로토타이핑, 벤치마크, 각종 기술 테스트를 한곳에 모아둔다.

> 이 저장소는 **제품 코드가 아니라 실험 기록**이다. 완성도보다 **재현성과 기록**을 우선한다.
> 실패한 실험도 지우지 않고 결론을 남긴다. "안 됐다"도 결과다.

## 디렉터리 구조

```
lab/
├── papers/           # 논문 리뷰 (읽고 정리한 것)
├── implementations/  # 논문/알고리즘 재구현 (from scratch)
├── experiments/      # 가설 검증용 단발성 실험
├── prototypes/       # 라이브러리·프레임워크·툴 사용 테스트
├── notes/            # 논문에 묶이지 않는 학습 노트, 정리글
├── shared/           # 여러 실험이 공유하는 유틸 (신중하게 추가)
└── templates/        # 새 실험을 시작할 때 복사하는 스캐폴드
```

각 카테고리 하위의 **프로젝트 1개 = 디렉터리 1개**이며, 서로 의존하지 않는다.
공통 코드가 필요해지면 복사부터 하고, 3번 이상 반복될 때만 `shared/`로 승격한다.

### 네이밍

| 카테고리 | 규칙 | 예시 |
|---|---|---|
| `papers/` | `{year}-{저자or약칭}-{키워드}` | `papers/2017-vaswani-attention/` |
| `implementations/` | `{모델·알고리즘명}` | `implementations/gpt2-from-scratch/` |
| `experiments/` | `{YYYYMMDD}-{짧은-가설}` | `experiments/20260919-rope-vs-alibi/` |
| `prototypes/` | `{기술명}` | `prototypes/duckdb-ingest/` |

## 프로젝트 하나의 구성

모든 실험 디렉터리는 **자기 완결적**이어야 한다. 루트에서 아무것도 설치하지 않아도 그 디렉터리만 보고 재현 가능해야 한다.

```
experiments/20260919-rope-vs-alibi/
├── README.md         # 필수. 아래 템플릿 참고
├── pyproject.toml    # 또는 requirements.txt / package.json — 의존성은 프로젝트 로컬
├── src/              # 코드
├── data/             # 입력 데이터 (대용량은 커밋하지 말고 받는 방법만 기록)
├── results/          # 지표, 로그, 그래프, 체크포인트 경로
└── notebooks/        # 탐색용 노트북 (결론은 README로 옮긴다)
```

### 프로젝트 README 템플릿

```markdown
# <제목>

- **상태**: 진행중 | 완료 | 보류 | 폐기
- **기간**: 2026-09-19 ~
- **원문/출처**: (논문 링크, arXiv ID, 블로그 등)

## 무엇을 / 왜
한 문단. 무슨 가설을 검증하는지, 왜 궁금했는지.

## 실행 방법
\`\`\`bash
uv sync && uv run python -m src.train
\`\`\`

## 결과
표나 그래프. 수치는 재현 가능한 형태로.

## 결론
알아낸 것 3줄 이내. 반증된 가설이면 그렇다고 명시.

## 남은 의문 / 다음에 할 것
```

새 실험은 `templates/`에서 복사해서 시작한다.

```bash
cp -r templates/python-experiment experiments/$(date +%Y%m%d)-my-idea
```

## 환경 관리

실험마다 스택이 다르므로 **루트에 공용 환경을 두지 않는다.**

- Python: 프로젝트별 `uv` (또는 venv). 버전은 `.python-version`에 고정.
- Node: 프로젝트별 `package.json`. 버전은 `.nvmrc`에 고정.
- 무거운 의존성(CUDA, 특정 드라이버 등)은 프로젝트 README의 "실행 방법"에 명시한다.

## 커밋 / 브랜치

- 브랜치를 나누지 않고 `main`에 바로 쌓아도 된다. 긴 실험만 `exp/<이름>`으로 분리.
- 커밋 메시지 접두사로 어느 실험인지 밝힌다.
  ```
  papers(attention): 리뷰 초안
  impl(gpt2): 어텐션 블록 구현
  exp(rope-vs-alibi): 1차 결과 기록
  ```

## 커밋하지 않는 것

- 대용량 데이터셋·체크포인트 — 다운로드 스크립트나 출처 링크로 대체
- API 키, 토큰, 자격증명 — `.env`는 무조건 gitignore, `.env.example`만 커밋
- 가상환경, `node_modules/`, 캐시, 노트북 실행 출력(가능하면 정리 후 커밋)

## 실험을 끝낼 때

1. README의 **상태**를 `완료` / `폐기`로 바꾼다.
2. **결론** 섹션을 채운다. 이게 이 저장소에 남는 진짜 자산이다.
3. 여러 실험에 걸쳐 일반화되는 교훈은 `notes/`에 따로 정리한다.

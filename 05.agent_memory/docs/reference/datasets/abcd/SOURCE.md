# ABCD (Action-Based Conversations Dataset) 원본

- 저장소: https://github.com/asappresearch/abcd (commit 6b8700ce67c6b37b062dd7a60abc76d7ef832a97)
- 논문: https://arxiv.org/abs/2104.00783 (Chen et al., NAACL 2021)
- 라이선스: MIT (`LICENSE`)
- 수집일: 2026-11-02
- 받은 파일 (저장소 `data/` 아래 원본 그대로, 수정 없음)

| 파일 | 내용 |
|---|---|
| `guidelines.json` | 상담원 가이드라인. flow 10개 (Product Defect, Order Issue, Account Access 등) → subflow |
| `kb.json` | 가이드라인이 참조하는 지식베이스 (계정 복구 절차 등) |
| `ontology.json` | intent·action·slot 정의 |
| `abcd_sample.json` | 샘플 대화 |
| `abcd_v1.1.json.gz` | 전체 대화. train 8,034 / dev 1,004 / test 1,004. 대화마다 `scenario`(고객·주문·상품 정보, flow/subflow), `original`(원문 발화), `delexed` |
| `README.md` | 저장소 README 원문 |

- `abcd_v1.1.json.gz`(약 37MB)는 git에 올리지 않는다 (`.gitignore`). 다시 받기:
  `curl -L -o abcd_v1.1.json.gz https://raw.githubusercontent.com/asappresearch/abcd/master/data/abcd_v1.1.json.gz`

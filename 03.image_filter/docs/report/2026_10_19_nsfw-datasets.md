# 공개 성인(NSFW) 이미지 데이터셋 / 벤치마크 조사

## 목적

이미지 검열 모델의 학습·평가에 쓸 수 있는 공개 데이터셋과 테스트셋이 있는지 확인한다.

## 방법

- 웹 검색으로 논문(arXiv), Hugging Face, GitHub를 조사했다 (2026-10-19).
- 데이터를 내려받거나 직접 확인하지는 않았다. 아래 수치는 각 출처에 적힌 값이다.

## 결과

### 평가(벤치마크)용

| 이름 | 규모 / 라벨 | 접근 | 비고 |
|---|---|---|---|
| UnsafeBench (2024) | 이미지 10,146장 (safe 6,098 / unsafe 4,048). 안전/위험 이진 라벨 + 위험 범주 11개 (Sexual 포함). 실사(LAION-5B) 5,060장 + AI 생성(Lexica) 5,086장 | HF gated, DUA 동의 필요 (승인에 1~2일) | 기존 분류기(NudeNet 등)와 VLM 분류기를 함께 비교한 논문이 있다. 라벨러 간 일치도가 Fleiss' κ 0.47로 중간 수준 [1][2] |
| Wukong-Demons (2025) | 생성 이미지에 단 NSFW 라벨, 범주 7개 (Sexual, Violence, Hate 등) | 공개 여부 미확인 | T2I 출력 검열용 [3] |

### 학습 + 평가용 (실사·성인 중심)

| 이름 | 규모 / 라벨 | 접근 | 비고 |
|---|---|---|---|
| LSPD (2022) | 50만 장 이상. porn / normal / sexy / hentai / drawings 분류 라벨 + 50,212장에 신체 부위 polygon 마스크 93,810개 | 연구자 요청 시 제공 [4] | 라벨이 가장 세밀하다 [4] |
| NudeNet (2019) | 분류(safe / sexy / nude) + 신체 부위 검출 | GitHub ([notAI-tech/NudeNet](https://github.com/notAI-tech/NudeNet)) | 데이터 공개 범위는 미확인 [4][5] |
| Adult content dataset (2017) | safe / adult | figshare (페이지 403으로 확인 못 함) | [4][6] |
| PEDA 376K | 37.6만 장, 포르노 검출용 | 미확인 | [7] |
| AIIA-PID4 (2013) | bikini / porn / skin / non-skin | 논문 PDF만 확인 | [5] |
| nsfw_data_scraper | 약 22만 장, porn / hentai / sexy / neutral / drawings | 이미지 대신 Reddit URL 목록과 수집 스크립트만 제공 | 라벨에 노이즈가 많아 README가 프로덕션 학습에 쓰지 말라고 경고한다. GantMan nsfw_model이 같은 5개 클래스로 학습했다 [8][9] |

### 영상 (프레임 추출 시 사용 가능)

- NPDI / Pornography-800: 영상 800개 (포르노 400 / 비포르노 400, 비포르노는 easy / difficult로 나뉨) [10]
- Pornography-2k: 영상 2,000개 (1,000 / 1,000). 포르노 프레임 중 상당수가 노골적인 장면이 아니라는 지적이 있다 [11]

### 비교 연구

- Akyon & Temizel (2023): Adult content / NudeNet / LSPD 세 데이터셋으로 CNN·ViT·SD safety checker·LAION 분류기를 비교했다. 결론은 "기존 평가셋이 부족하니 더 다양하고 어려운 벤치마크가 필요하다" [4]
- UnsafeBench: 실사로 학습한 분류기는 AI 생성 이미지에서 성능이 떨어진다 (분포 차이) [1]
- 모델 카드의 자체 보고 수치(예: Marqo 98.56%)는 비공개 데이터 기준이라 다른 모델과 직접 비교할 수 없다 [12]

## 애니 데이터 (메인 대상, 2차 조사)

### 후보

| 이름 | 규모 / 라벨 | 접근 | 비고 |
|---|---|---|---|
| p1atdev/danbooru-2024 | 메타데이터 8,042,822건 (다운로드 6.5GB). `rating` + 태그(general / character / copyright / artist / meta) + 이미지 URL | HF, 라이선스 표기 없음 | 이미지 파일은 없다. 태그로 거른 뒤 URL에서 받는 구조라 제외 필터를 먼저 걸 수 있다 [14] |
| deepghs/danbooru2024 계열 | 원본 / WebP 4MP 압축 / SFW 판 | HF | 스키마는 확인 못 함 [15] |
| Danbooru2021 (gwern) | 490만 장 이상, 태그 1.62억 개. 등급 s / q / e 비율 약 77 / 15 / 10% | 내려진 상태로 표기 | 업로더가 애매하면 q를 고르는 경향이 있다 [16] |
| deepghs/nsfw_detect | 1만~10만 장, 이미지 분류 | HF, MIT, Not-For-All-Audiences | 라벨 체계와 출처는 카드에 없다. 미성년 필터 언급도 없다 [17] |
| deepghs/anime_rating (모델) | safe / r15 / r18. 정확도 64.8~74.3% | HF, MIT | 학습 데이터를 수동 필터 없이 스크래핑했다고 밝힌다. 등급 경계가 모호해 정확도가 낮다. 기준선 모델로 쓸 수 있다 [18] |
| AnimeDL-2M | 애니 이미지 200만 장 이상 (실사·조작·AI 생성) | 공개 | NSFW 라벨은 없다. AI 생성 / 조작 검출용 [19] |
| GantMan nsfw_model | drawings / hentai 클래스 포함, 5개 클래스 | GitHub | 기준선 모델 [9] |

### 아동 성착취물 위험

- Danbooru는 성적 콘텐츠를 금지하지 않고 등급으로만 나눈다 [16]. 미성년으로 보이는 캐릭터의 성적 이미지가 원본에 섞여 있다.
- 한국 아청법은 "아동·청소년으로 명백하게 인식될 수 있는" 표현물도 성착취물에 포함한다. 그런 이미지는 받기 전에 걸러야 한다.
- 메타데이터를 먼저 받으면 이미지를 받기 전에 태그로 제외할 수 있다. 다만 태그가 빠진 이미지는 걸러지지 않는다.

### 수집 방안 (제안)

1. danbooru-2024 메타데이터(parquet)만 받는다. 이미지는 아직 받지 않는다.
2. 제외 필터를 적용한다: 미성년 관련 태그(loli, shota, child, 학생 계열 등)가 있는 게시물은 등급과 상관없이 전부 뺀다. 미성년 외형 관련 태그도 보수적으로 넓게 잡는다.
3. 등급별로 균형 있게 뽑는다 (g / s / q / e). 실사·AI 생성 비율 같은 다양성 축도 정한다.
4. 처음 받는 이미지는 소량(예: 등급당 수백 장)으로 한정하고, 해시 대조와 사람 검수를 거친다.

## GantMan 데이터 (nsfw_data_scraper) 확인

- 저장소: alex000kim/nsfw_data_scraper (MIT). 이미지는 없고 클래스별 URL 목록만 있다.
- URL 수: drawings 15,566 / hentai 4,611 / neutral 36,837 / porn 57,289 / sexy 15,957 (합계 130,260)
- 주요 호스트: drawings·hentai·neutral·sexy는 i.imgur.com / i.redd.it, porn은 cdn.pornpics.com이 97.7%
- 수집 출처: hentai는 r/hentai, r/ecchi, r/sukebei 등, drawings는 r/anime, r/awwnime 등 애니 서브레딧
- 생존율 (클래스별 1% 표본 중 40개를 HEAD 요청으로 확인, 2026-10-19):

| 클래스 | 살아 있음 |
|---|---|
| drawings | 37/40 |
| hentai | 20/40 |
| neutral | 35/40 |
| sexy | 14/40 |
| porn | 1/40 |

- imgur는 지운 이미지를 `removed.png`(200)로 리다이렉트한다. 상태 코드만 보면 살아 있는 것처럼 보이므로 최종 URL로 판정했다.
- porn은 거의 다 죽었다. 실사 성인 클래스는 다른 출처가 필요하다.
- 애니 쪽(drawings 약 1.4만, hentai 약 2,300장 추정)은 아직 쓸 수 있다.
- 첫 수집 (2026-10-20, `fetch_gantman.py --per-class 200`): drawings 261장 / hentai 181장, 각각 URL 400개 시도
  - 목표와 수가 다른 이유: 배치를 크게 잡아 drawings는 초과, hentai는 같은 이미지(md5 중복)를 성공으로 세어 미달. 스크립트를 파일 수 기준으로 고침
  - hentai 사람 검수는 아직 안 함
- 아동 성착취물 위험: hentai 출처 서브레딧에 미성년으로 보이는 캐릭터가 섞여 있을 수 있다. 태그가 없어 미리 거를 수 없으므로 받은 뒤 사람이 검수해야 한다.

## 해석

- 표준이라고 할 만한 단일 공개 테스트셋은 없다.
- 평가 기준선에는 UnsafeBench(Sexual 범주)가 가장 쓰기 쉽다: 라벨이 붙어 있고 HF에서 바로 받을 수 있다.
- 실사 성인 이미지를 세밀하게 나눈 학습 데이터로는 LSPD가 가장 적합하다 (요청 필요).
- 웹에서 긁어 온 데이터(LAION 계열, scraper)에는 불법 콘텐츠가 섞일 위험이 있다. LAION-5B에서 CSAM 의심 링크가 발견되어 Re-LAION-5B로 2,236개 링크가 제거됐다 [13]. 직접 수집할 때는 출처를 성인이 확인된 곳으로 제한하고, 해시 매칭(PhotoDNA 등) 같은 차단 절차를 먼저 정해야 한다.

## 남은 질문

- LSPD 신청 절차와 라이선스 (상업적 사용 가능 여부)
- 검열 라벨 체계: 이진(safe/nsfw)으로 할지, 다중 클래스(sexy / porn / hentai 구분)로 할지
- 그림(drawings / hentai)을 대상에 포함할지

## 출처

1. Qu et al., UnsafeBench, arXiv:2405.03486 — https://arxiv.org/abs/2405.03486
2. UnsafeBench HF 데이터셋 — https://huggingface.co/datasets/yiting/UnsafeBench
3. Wukong Framework for NSFW Detection in T2I, arXiv:2508.00591 — https://arxiv.org/abs/2508.00591
4. Akyon & Temizel, State-of-the-Art in Nudity Classification, arXiv:2312.16338 — https://arxiv.org/abs/2312.16338
5. fcakyon/content-moderation-deep-learning (데이터셋 목록) — https://github.com/fcakyon/content-moderation-deep-learning
6. Adult content dataset (figshare) — https://figshare.com/articles/dataset/Adult_content_dataset/13456484 (직접 확인 못 함)
7. PEDA 376K — https://digitalcommons.uri.edu/cs_facpubs/25 (초록만 확인)
8. nsfw_data_scraper (포크) — https://github.com/Mak0760/nsfw_data_scraper (원본 alex000kim 저장소는 확인 못 함, 2차 자료)
9. GantMan/nsfw_model — https://github.com/GantMan/nsfw_model
10. Moustafa, Applying deep learning to classify pornographic images and videos, arXiv:1511.08899 — https://arxiv.org/abs/1511.08899
11. Detecting sexually explicit content in the context of CSAM, arXiv:2406.14131 — https://arxiv.org/abs/2406.14131
12. Marqo/nsfw-image-detection-384 모델 카드 — https://huggingface.co/Marqo/nsfw-image-detection-384
13. LAION, Releasing Re-LAION-5B — https://laion.ai/blog/relaion-5b/
14. p1atdev/danbooru-2024 — https://huggingface.co/datasets/p1atdev/danbooru-2024
15. deepghs (HF) — https://huggingface.co/deepghs
16. gwern, Danbooru2021 — https://gwern.net/danbooru2021
17. deepghs/nsfw_detect — https://huggingface.co/datasets/deepghs/nsfw_detect
18. deepghs/anime_rating — https://huggingface.co/deepghs/anime_rating
19. AnimeDL-2M, arXiv:2504.11015 — https://arxiv.org/abs/2504.11015

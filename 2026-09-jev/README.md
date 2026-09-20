# JEV (TypeSafe AI) — System One Model 조사

- **질문**: Jev는 정말 새로운 모델 클래스인가, 아니면 constrained decoding의 리브랜딩인가?
  그리고 실제로 "LLM 분류/라우팅 호출 대체" 용도로 쓸 만한가?
- **상태**: 진행중 (자료 수집 완료, 실측 미실시)
- **결론**: (잠정) 아이디어는 진짜지만 검증은 아직 없음.
  비autoregressive + calibration 학습(RLCD)이라는 주장은 **논문/가중치/독립 재현이 전무**.
  속도·비용 우위는 서드파티 테스트에서도 살아남지만 배율은 마케팅(193x/444x)보다
  훨씬 작음(실측 1.6x~58x). 정확도는 프론티어 대비 5%p 정도 아래.

## 배경

- 2026-09-15 TypeSafe AI 출시. 창업자 Diego Almeida (前 OpenAI, ChatGPT/RLHF 참여).
- "System One Model" = Kahneman의 System 1에서 따온 이름.
  사람과 대화하는 모델이 아니라 **소프트웨어 안에서 판단만 내리는** 모델.
- 한 줄 요약: `unstructured state in → typed probabilistic decisions out`

## 자료

| 파일 | 내용 |
|---|---|
| [자료/01-개요.md](자료/01-개요.md) | 무엇인가, 왜 나왔나, 포지셔닝 |
| [자료/02-아키텍처-학습.md](자료/02-아키텍처-학습.md) | parallel sampler, RLCD, 알려진 것 / 모르는 것 |
| [자료/03-API-사용법.md](자료/03-API-사용법.md) | 엔드포인트, 3개 프리미티브, SDK, 제약 |
| [자료/04-벤치마크-검증.md](자료/04-벤치마크-검증.md) | 공식 수치 vs 독립 테스트, 방법론 비판 |
| [자료/05-생태계.md](자료/05-생태계.md) | SDK/통합/오픈소스 복제 프로젝트 링크 모음 |
| [자료/06-이론-단일토큰-readout.md](자료/06-이론-단일토큰-readout.md) | readout의 이론 — 베이즈 조건화, LM head 구조, calibration, RLCD 반증 예측 |

## 구현

| 파일 | 내용 |
|---|---|
| [baseline-qwen3-readout.ipynb](baseline-qwen3-readout.ipynb) | **귀무가설 구현.** Qwen3-1.7B + 단일토큰 readout — forward 1회 판정, KV 캐시 공유 레이턴시 측정, 군별 temperature scaling + ECE, 마스크 은닉 테스트 |
| └ §12 캐릭터 채팅 | **실전 케이스.** 이미지 200개 중 턴마다 1개 선택 — `AA`/`AB` 단일토큰 라벨, 카탈로그 KV prefix, 턴별 마스킹, **위치 편향 실험** |

## 다음에 할 것

- [x] 귀무가설(constrained decoding 베이스라인) 구현 → `baseline-qwen3-readout.ipynb`
- [x] readout 이론 정리 → `자료/06-이론-단일토큰-readout.md`
- [ ] **§12-4 위치 편향 실험** ← 최우선. 200줄 카탈로그를 1.7B가 실제로 읽는지가 갈림길.
      실패 시 대안: 코드로 26개 압축 / 2단계 임베딩 / 로그 LoRA
- [ ] **노트북 실행** (모델 forward는 아직 미실행) — 셀 4 채팅 템플릿, 셀 6 토큰 충돌이 확인 지점
- [ ] 실제 캐릭터 데이터로 `CATALOG`/`TURNS` 교체
- [ ] 토이 데이터를 실제 도메인 데이터로 교체 (태스크군당 수백 건, held-out 분리)
- [ ] 0.6B / 1.7B / 4B 정확도-레이턴시 곡선
- [ ] early access 대기열 등록 → 실제 API 키 확보
- [ ] Jev vs 베이스라인: **정확도 아니라 ECE부터** 비교
- [ ] 판별 테스트 — 정답을 후보에서 뺐을 때 Jev의 confidence가 떨어지는가
      (안 떨어지면 RLCD는 마케팅. 06 문서 §6 예측 2)
- [ ] 멀티태스크 LoRA: 여러 레이블 세트를 섞어 클래스가 아니라 포맷/스킬을 학습
- [ ] 오픈소스 복제본(NanoJev, Laya) 코드 읽고 "parallel sampler" 실체 역추정
- [ ] (보류) 이미지 입력 — Qwen3-VL-2B 포팅. readout 코드는 거의 그대로 가고 셀 3·4만 바뀜.
      Jev가 텍스트 전용이라 비교 깨짐 → 텍스트판은 비교용으로 유지할 것

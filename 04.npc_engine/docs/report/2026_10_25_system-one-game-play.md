# System One 모델로 게임을 플레이하는 방식 — 사례 조사

## 목적

- Jev 같은 System One 모델(텍스트 생성 없이 선택지 확률만 반환)로 NPC 행동을 정하려 한다.
- 게임 플레이 사례들이 어떤 state를 넣고, 어떤 질문을 하며, 답을 어떻게 입력(상하좌우 등)으로 바꾸는지 정리한다.
- 모델 자체 개념은 `01.jev/docs/notes/` 참고 (Choice / Noul / Score, calibration, Laya 구조).

## 방법

- Jev 출시(2026-09-15) 이후 공개된 게임 데모·저장소·블로그를 웹 검색으로 수집
- README와 블로그를 직접 읽고 state 형식·질문·행동 매핑·지연시간·결과를 뽑음
- 상하좌우 선택에 가장 가까운 Snake 구현은 소스까지 확인 → [prompt.ts 원문](../reference/spatial-src/prompt_typesafe-snake.ts)
- 수치는 전부 각 저장소·블로그의 자체 보고. 독립 재현은 하지 않음

## 결과

### 사례 요약

| 사례 | 게임 | state | 질문 / 선택지 | 결과 (자체 보고) |
|---|---|---|---|---|
| [TypeSafe 공식 Doom 데모](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) | Doom | 플레이어 상태를 구조화한 데이터 (픽셀 아님) | 매 틱 작은 질문 여러 개 (방아쇠·목표·회피 등, 2차 자료) | 약 10 결정/초, 응답 0.114s vs 범용 LLM 8.6s |
| [jev-plays-doom](https://github.com/tirukovelamanoj/jev-plays-doom) | ViZDoom | JSON: 체력·탄약·방향 + 가까운 순 몬스터 `{kind, distance, bearing_deg}` | `action` Choice {ATTACK, TURN_LEFT, TURN_RIGHT} + `in_danger` Noul | 20판 평균 6.55킬, 손으로 짠 조준 코드와 동일. 평균 212ms |
| [doom-war](https://github.com/rythmn1111/doom-war) | ViZDoom 데스매치 | depth buffer로 만든 짧은 문장 (`ahead: wide open, left: tight`), 라이벌 조준 여부 | 질문 7개: goal / target / turn / movement / trigger / dodge / danger | Laya(322M, 로컬) 5:1 Jev. Laya 결정 수 2배, 대신 shield 교정률 88% vs 31% |
| [blocks.ai 오픈 모델 재현](https://blocks.ai/blog/jev-open-model-doom) | ViZDoom | 엔진 변수 → 짧은 텍스트 요약 | 3~4개 행동. 전체 맵은 코드가 단계(combat/stuck/navigate) 판정 + BFS 경유지, 모델은 국소 방향만 | Gemma 4 12B base, forward 1회로 A~Z logit 읽기. p50 113ms (M4) |
| [doom-jev](https://github.com/AmoghCreator/doom-jev) | ViZDoom | YAML 상황 보고 (체력·무기·보이는 적·장애물) | 큰 목표 / 대상 / 이동 / 회전 / 점프 / 사격 | 추론 비동기 약 10Hz, 게임 35 tic/s. 그 사이엔 기하 계산으로 조준 유지. 게임 결과 수치 없음 |
| [typesafe-snake](https://github.com/sorrycc/typesafe-snake) | Snake | 격자 문자열 + 머리·먹이 좌표·진행 방향·길이 | Choice 하나. 선택지 = 안전한 방향들, 각 방향에 코드가 계산한 사실 설명 | 마감 안에 답이 없으면 직진. 수치 없음 |
| [Laya vs Jev Snake](https://systemonemodels.org/examples/videos/local-laya-vs-cloud-jev-snake/) | Snake | 미공개 | 동일 질문 | Laya 421M 로컬 15.3ms·점수 46, Jev 클라우드 298ms·점수 1 |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | Maze, Snake, ViZDoom | 텍스트 state + 후보 행동 (Doom은 보이는 물체 라벨 bbox + 최근 4프레임) | Doom: {left, right, shoot, noop}. Maze: 안 가본 방향만. Snake: 역방향 제외 전부 | Qwen3-0.6B 미세조정. ViZDoom Basic 128/128 vs Jev 56/128, Maze 4/10 vs Jev 7/10 |
| [CLM T-Rex](https://github.com/Contrastive-LM/CLM/tree/main/examples/t_rex) | Chrome 공룡 | 한 줄: "2 large cacti ahead, 96 px away." | {jump, duck, run}, 각 선택지에 물리 플래너가 판정한 safe/unsafe 설명 | 60FPS, 요청 여러 개를 몇 프레임 간격으로 동시에 보냄 |
| [minecraft-agent](https://github.com/rmalde/minecraft-agent) | Minecraft | 게임 관찰 (세부 미공개) | 사용 가능한 행동 하나 (이동·채굴·제작·전투 등) | 느린 플래너(Astra)가 목표 지정, Jev는 약 4초에 1회 실행 선택. 엔더 드래곤 8분 43초 |

### Snake 예시 — 상하좌우를 고르는 형태

[typesafe-snake](https://github.com/sorrycc/typesafe-snake)의 요청 구조 (원문 [prompt.ts](../reference/spatial-src/prompt_typesafe-snake.ts)):

```
state = {
  board: ["....F...", "..Hoo...", ...],      # 격자 문자열
  legend: "H = head, o = body, T = tail, F = food ...",
  head: {row, col}, food: {row, col}, heading, snakeLength, gridSize,
  foodIsAdjacent: bool,
}
instructions = 게임 규칙 + 전략 프리셋 (safe / greedy / chaos)
criteria = {                                  # 선택지 = 방향, 설명 = 코드가 계산한 사실
  "up":   "straight, head moves to row 3 col 5; food is 4 steps away; 40 of 52 empty cells stay reachable",
  "left": "turn left, ...; DEAD END: less room than the snake is long ...",
}
```

- 선택지에는 이번 한 걸음이 안전한 방향만 넣는다 (벽·몸통 충돌은 코드가 미리 제거)
- 각 방향의 결과(먹이 거리, flood fill로 센 도달 가능 칸 수, 막다른 길 여부)를 코드가 계산해 선택지 설명에 적는다
- 모델은 "어느 방향이 좋은가"라는 의미 판단만 한다

### 반복해서 나오는 설계 패턴

1. 픽셀이 아니라 텍스트 state
   - 모든 사례가 엔진 변수(좌표·체력·물체 라벨·depth)를 JSON/YAML/짧은 문장으로 바꿔 넣는다.
   - 숫자를 날것으로 주기보다 의미를 붙인다: "LINED UP IN THE SIGHTS", "DEAD END", "safe / unsafe".
2. 선택지는 작은 이산 집합
   - 3~5개 방향·버튼 (상하좌우, 좌회전/우회전/사격). 연속값(벡터)은 코드가 만든다.
   - 선택지 설명(criteria)에 각 행동의 결과를 미리 적으면 정확도가 크게 오른다.
     - jev-plays-doom: 사격 기준을 선택지에 숫자로 적으면 평균 6.2킬, 의도만 적으면 −0.6킬 (ATTACK 선택 0회)
3. 결정 하나를 여러 질문으로 쪼갠다
   - goal / movement / turn / trigger / dodge 같은 질문을 한 요청에 묶는다. 질문끼리 독립 평가라 지연이 거의 안 늘어남 (Jev 기준).
   - 질문 간 의존이 필요하면 코드가 엮는다.
4. 코드가 앞뒤를 감싼다
   - 앞: 합법 행동 생성, 경로(BFS), 거리·각도 계산
   - 뒤: shield (실탄 없음·벽으로 이동 같은 명백한 오답 교정), 회전량 분배, 버튼 벡터로 변환
   - 예: doom-jev는 선택 결과를 8채널 버튼 벡터 `[ATK, FWD, BCK, L, R, TL, TR, JMP]`로 바꿈
5. 게임 루프와 추론 분리
   - 게임은 35~60fps, 모델은 3~90 결정/초. 비동기로 마지막 결정을 유지하거나, 마감 지나면 기본 행동(직진)
   - confidence가 낮으면 규칙 기반으로 넘어감 (jev-plays-doom `--conf-floor`)
6. 느린 층 + 빠른 층
   - 전체 경로·목표는 코드(BFS)나 느린 LLM 플래너, System One은 국소 선택만 (blocks.ai, minecraft-agent)

### 모델 사용 방식 3가지

| 방식 | 사례 | 장단점 |
|---|---|---|
| 호스팅 Jev API | 공식 데모, jev-plays-doom, typesafe-snake | 학습 불필요. 네트워크 왕복으로 200~600ms |
| 오픈 모델 + logit readout / 판단 head | Laya, blocks.ai (Gemma), CLM | 로컬 15~150ms, 무료. 처음 보는 질문엔 정확도가 떨어짐 (Laya shield 교정 88%) |
| 게임 데이터로 미세조정 | NanoJev (Qwen3-0.6B, 질문 1.9만 개, 레이블 = Jev 답 + 실제 결과) | 해당 게임에선 Jev를 넘기도 함. 게임마다 데이터 필요 |

## 해석 — NPC 엔진에 적용하면

- "환경·상황 → state, 결과 → 상하좌우"라는 구상은 Snake·Doom 사례와 같은 구조다. 바로 시도해 볼 만하다.
- 다만 사례들에서 모델이 혼자 잘하지는 않았다. 성능의 상당 부분이 코드에서 나온다:
  - 선택지를 합법 행동으로 줄이기
  - 각 선택지의 결과를 계산해 설명에 넣기
  - shield로 명백한 실수 막기
- NPC 반응 속도가 중요하면 로컬 모델(Laya 등)이 유리하다. 이미 `01.jev/laya-typed-decisions`에 Laya 학습·평가 스크립트가 있다.
- 최소 프로토타입 안:
  - 격자 월드 + NPC 1명 + 자극(플레이어 접근, 소리, 아이템)
  - state = 격자 문자열 + 주변 사실, 질문 = `move` Choice {up, down, left, right, stay} + `threatened` Noul
  - 선택지 설명에 "이 방향으로 가면 플레이어와 거리 N" 같은 사실을 코드로 계산해 넣기
  - 비교: 선택지 설명 있음 vs 없음, Laya vs Jev, shield 있음 vs 없음

## 남은 질문

- 공식 Doom 데모의 정확한 질문 목록 (공식 문서에서 확인 못 함. LinkedIn 2차 자료뿐)
- 연속 벡터 출력 사례는 못 찾음. 모든 사례가 이산 선택 → 코드가 벡터로 변환
- 이미지 입력: NanoJev는 "향후 확장", Valen(이미지 입력 복제 모델, `01.jev` 노트 02)은 게임 사례 미확인
- 여러 NPC를 한 번에 판단할 때(배치) 지연: arena 사례(30 결정/초, Laya 21ms)는 X 게시물 요약뿐

## 출처

- [The Register — TypeSafe AI debuts model that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)
- [DataCamp — Jev 설명](https://www.datacamp.com/blog/system-one-models-jev) (공식 데모 10 결정/초·시간당 약 $7, 검색 요약 기준)
- [tirukovelamanoj/jev-plays-doom](https://github.com/tirukovelamanoj/jev-plays-doom)
- [rythmn1111/doom-war](https://github.com/rythmn1111/doom-war)
- [blocks.ai — We Rebuilt Jev's API on an Open Model and Used It to Play Doom](https://blocks.ai/blog/jev-open-model-doom)
- [AmoghCreator/doom-jev](https://github.com/AmoghCreator/doom-jev)
- [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake) — [prompt.ts 원문](../reference/spatial-src/prompt_typesafe-snake.ts)
- [Local Laya vs Cloud Jev Snake](https://systemonemodels.org/examples/videos/local-laya-vs-cloud-jev-snake/) (X 게시물 요약)
- [Jev vs Laya arena survival](https://systemonemodels.org/examples/discussions/jev-vs-laya-arena-survival-game/) (X 게시물 요약)
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev), [UNIFIED_GAMES.md](https://github.com/TianyuCodings/NanoJev/blob/main/docs/UNIFIED_GAMES.md)
- [Contrastive-LM/CLM T-Rex 예제](https://github.com/Contrastive-LM/CLM/tree/main/examples/t_rex)
- [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent)
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) (사례 목록)

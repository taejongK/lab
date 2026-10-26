# System One 게임 사례 — 공간 정보를 state에 넣는 방법

## 목적

- System One 모델(Jev·Laya류)로 게임을 하는 사례들이 위치·방향·벽·적 같은 공간 정보를 어떻게 텍스트 state로 바꿨는지 코드 수준에서 확인한다.
- 이전 보고서: [System One 모델 게임 플레이 사례](2026_10_25_system-one-game-play.md)

## 방법

- 공간 직렬화 코드를 공개한 저장소 5개의 소스를 직접 읽음. 원문은 [spatial-src/](../reference/spatial-src/)에 저장
  - typesafe-snake (`prompt.ts`, `analysis.ts`) — 격자
  - NanoJev (`unified_grid_envs.py`, `evaluate_composed_maze.py`, `unified_doom_env.py`) — 격자 미로·Doom
  - jev-plays-doom (`doom_agent.py`) — 3D
  - doom-war (`observe.py`) — 3D
  - doom-jev (`state_serializer.py`) — 3D
- 소스 없이 글로만 본 것: blocks.ai 블로그, CLM T-Rex README
- 아래 코드 블록의 고정 문구·형식은 원문 그대로이고, 숫자·격자 내용은 형식을 보여 주려고 만든 예시 값 (jev-plays-doom JSON만 README의 실제 예시)

## 결과

### 공통 원칙

- 모델은 픽셀도, 좌표 계산도 하지 않는다. 기하 계산은 전부 코드가 하고 결과를 글로 넘긴다.
  - doom-war `observe.py` 첫 줄: "The model never sees pixels or raw coordinates. Deterministic code does the geometry and hands over short descriptions; the model only ranks them."
- 차이는 "얼마나 가공해서 넘기느냐"다. 아래 표는 가공이 적은 것부터 많은 것 순서.

### 표현 방식 8가지

| # | 방식 | 사례 | 모델이 받는 것 |
|---|---|---|---|
| 1 | 화면 좌표 bbox | NanoJev Doom | 보이는 물체 `{name, bbox: [x,y,w,h]}` + 화면 크기 320×240 + 플레이어 위치·각도 |
| 2 | 전체 격자 ASCII | typesafe-snake | 격자 문자열 전체 + 범례 + 머리·먹이 좌표 |
| 3 | 에이전트 중심 국소 창 | NanoJev Maze | 5×5 ASCII 창 (가운데 A) + 탐험 기록 비트마스크 |
| 4 | 자기중심 극좌표 (숫자) | jev-plays-doom | 적마다 `distance`, `bearing_deg` + 부호 규약 설명 |
| 5 | 자기중심 극좌표 (구간 단어) | doom-war, doom-jev | "close, slightly left", "medium (ahead right)" |
| 6 | 방향별 여유 공간 | doom-war, doom-jev | `space: {ahead: wide open, left: tight, right: blocked}` |
| 7 | 1차원 거리 한 줄 | CLM T-Rex | "2 large cacti ahead, 96 px away." |
| 8 | 공간 결과를 선택지 설명에 | typesafe-snake, NanoJev Maze, T-Rex | 방향마다 "도착 좌표, 먹이 거리, 남는 빈칸 수, 막다른 길" |

#### 1. 화면 좌표 bbox — NanoJev Doom

```
visible_labels: [{"id": 3, "name": "Cacodemon", "bbox": [141, 98, 37, 40]}, ...]
screen_size: [320, 240], bbox_format: "x,y,width,height; origin top left"
health, ammo, position [x,y,z], angle, 최근 관찰 최대 4프레임
선택지: left / right / shoot / noop ("Strafe left for N Doom ticks.")
```

- 가장 덜 가공된 형태. "화면 중앙에 가까운가"를 모델이 bbox 숫자로 추론해야 한다.
- 그래서인지 NanoJev는 이 형태로 Qwen3-0.6B를 미세조정했다. 학습 없이 쓰는 사례는 이 방식을 안 씀.

#### 2. 전체 격자 ASCII — typesafe-snake

```
board: ["..........", "...Hoo....", "......F...", ...]
legend: "H = snake head, o = snake body, T = snake tail, F = food, . = empty.
         Row 0 is the top row, column 0 is the leftmost column. Leaving the grid hits a wall."
head: {row, col}, food: {row, col}, heading: "right", snakeLength, gridSize
```

- 격자 + 좌표를 둘 다 준다. 좌표계(행 0 = 위)를 글로 명시.
- 실제 판단 근거는 격자보다 8번(선택지 설명)에 있다.

#### 3. 에이전트 중심 국소 창 + 탐험 기억 — NanoJev Maze

```
Agent coordinate: (3,4); zero-based row and column. Rows increase south; columns increase east.
The local window is centered on A. '#': wall; '.': open; 'A': agent; 'X': outside.
Local map:
#.#..
#.#.#
..A..
##.##
XXXXX
Current direction memory: {"north": "open", "east": "untried", "south": "blocked", "west": "untried"}
Complete observed edge memory ... Bits: north=1, east=2, south=4, west=8.
0:00x3,31,00
1:...
```

- 전체 지도 대신 주변 5×5만 준다 (3×3도 지원). 맵 밖은 `X`.
- 안 보이는 부분은 "가 본 칸에서 시도한 방향 / 열린 방향" 비트마스크로 행마다 압축해 기억으로 넣는다. `00`은 "벽"이 아니라 "정보 없음"이라고 명시.
- 선택지는 아직 안 가 본 방향만. 다 막히면 코드가 가까운 미탐험 지점으로 자동 이동.

#### 4. 자기중심 극좌표 (숫자) — jev-plays-doom

```json
{
  "health": 100, "ammo": 26, "facing_deg": 0,
  "monsters_nearest_first": [
    {"kind": "Demon", "distance": 244, "bearing_deg": -163},
    {"kind": "Demon", "distance": 283, "bearing_deg": 90}
  ],
  "note": "bearing 0 = dead ahead. POSITIVE bearing means the monster is to your LEFT (turn left to face it); NEGATIVE means to your RIGHT."
}
```

- 절대 좌표 (x, y) 대신 "내가 보는 방향 기준 각도 + 거리"로 바꾼다. 행동(좌회전/우회전)과 직접 대응되기 때문.
- 계산: `bearing = (atan2(dy, dx) − 내 각도 + 540) % 360 − 180`
- 부호 규약을 state 안에 글로 넣는다.

#### 5. 자기중심 극좌표 (구간 단어) — doom-war, doom-jev

doom-war:

```
threats: ["imp, close slightly left, in sight",
          "rival, mid range dead ahead, LINED UP IN THE SIGHTS, 512 units"]
rival: "LINED UP IN THE SIGHTS, 512 units away — SHOOT NOW"
```

- 각도 → `dead ahead (±12°) / slightly left·right (±60°) / to the left·right (±120°) / behind`
- 거리 → `right on top (<150) / close (<400) / mid range (<900) / far off`
- 조준 원뿔(±25°) 안이고 사거리 안이면 "LINED UP IN THE SIGHTS" 플래그

doom-jev는 숫자와 단어를 같이 준다 (YAML):

```yaml
enemies:
  - label: DoomImp
    distance: 300 (medium)
    bearing: -30 deg (ahead right)
    occluded: false
```

#### 6. 방향별 여유 공간 — doom-war, doom-jev

- doom-war: depth buffer의 눈높이 띠(화면 높이 42~62%)를 좌·중·우로 잘라 최솟값 → `blocked (<16) / tight (<40) / some room (<100) / wide open`
- doom-jev: depth buffer 중앙값 + 맵 벽 선분에 레이캐스트(정면, ±40°) → `wall_directly_ahead / wall_left / wall_right: true|false`
- doom-war 주석: 이게 없을 때 "두 파이터가 벽으로 걸어가 거기 서 있었다. state에 벽이 있다는 말이 없었으니까."

#### 7. 1차원 거리 한 줄 — CLM T-Rex

- `"Dino runner game. 2 large cacti ahead, 96 px away."` 끝.
- 판단은 8번 방식으로 넘긴다: 물리 플래너가 jump/duck/run 각각을 "Safe. Clears the 2 large cacti. Best." / "Unsafe. Hits ..." 로 미리 판정.

#### 8. 공간 결과를 선택지 설명에 넣기 — 가장 많이 쓰이고 효과가 큰 방식

typesafe-snake `analysis.ts`가 방향마다 계산하는 것:

| 항목 | 계산 |
|---|---|
| turn | 현재 진행 방향 기준 straight / left turn / right turn |
| target | 이동 후 머리 좌표 |
| foodDistance | 이동 후 먹이까지 맨해튼 거리 |
| reachable / freeTotal | 이동 후 flood fill로 닿는 빈칸 수 / 전체 빈칸 |
| deadEnd | 닿는 공간 < 몸 길이이고 꼬리로도 못 빠져나감 |

모델이 받는 선택지:

```
"up":   "straight, head moves to row 3 col 5; food is 4 steps away after this move; 40 of 52 empty cells stay reachable; can still follow its own tail out"
"left": "left turn, head moves to row 4 col 4; food is 6 steps away after this move; 3 of 52 empty cells stay reachable; DEAD END: ..."
```

- 공간 추론(경로·막힘·거리 변화)을 코드가 끝내고, 모델은 "어떤 결과가 더 좋은가"만 고른다.
- 그 밖의 예: NanoJev Maze "Attempt one cell north to [2,4]; this direction has not been tried here." / jev-plays-doom의 rule criteria("bearing이 −8~+8이면 ATTACK")

### 사례에서 나온 시행착오

| 문제 | 원인 | 해결 | 출처 |
|---|---|---|---|
| 적 주위를 빙빙 돎 | bearing 부호 반전 (atan2는 +가 왼쪽, 엔진 회전 입력은 +가 오른쪽) | 부호 규약 통일 + state에 글로 명시 | blocks.ai, doom-war `motor.py` |
| 제자리에서 좌우로 흔들림 | 적을 bearing 순으로 정렬 → 돌 때마다 목표가 바뀜 | 거리 순 정렬 | jev-plays-doom 주석 |
| 바로 옆 적을 state가 모름 | 렌더러 라벨 목록이 너무 가깝거나 화면 끝 물체를 놓침 | 라벨 대신 기하(각도·거리)로 조준 여부 판정 | doom-war 주석 |
| 벽에 박혀 안 움직임 | state에 벽 정보 없음 | depth로 방향별 여유 공간 추가 | doom-war 주석 |
| 방향을 매번 바꿈, stuck 33회 | 매 틱 "어느 쪽이 열려 있나"를 모델에게 물음 | 코드가 BFS 격자로 경유지 계산, 모델은 국소 방향만 → stuck 3회 | blocks.ai |
| 사격을 안 함 (평균 −0.6킬) | bearing 숫자만 주고 "언제 쏠지"는 모델에게 맡김 | 선택지에 숫자 기준 명시 → 6.2킬 | jev-plays-doom README |
| 229발 쏴서 0킬 | 사격 거리 700 — 먼 적은 화면에 너무 작음 | 거리 기준 조정 | blocks.ai |

### 격자·이미지로 직접 넣은 사례 (추가 조사)

#### 격자 텍스트 — NanoJev의 비교 실험

NanoJev는 격자를 텍스트로 넣는 방식을 실제로 비교했다. 표현만 바꾼 비교 결과가 있는 유일한 사례.

1. 전체 지도 ASCII를 넣고 다음 행동을 바로 고르게 함 ([DEVELOPMENT_RESULTS](../reference/spatial-src/DEVELOPMENT_RESULTS_nanojev.md))
   - 8×8 / 16×16 / 50×50 미로 3개, 128걸음 제한
   - Jev와 학습 모델 모두 0/3. 최단 경로 코드만 3/3
2. 주변 5×5 ASCII + 원자 질문 4개 + 코드 플래너 ([ATOMIC_PLANNING](../reference/spatial-src/ATOMIC_PLANNING_nanojev.md))
   - 질문: "북/동/남/서로 한 칸 가면 지나갈 수 있나?" (Noul 4개 병렬)
   - 모델은 국소 판단만. 어느 방향으로 갈지는 코드가 확률 + 목표 거리 + 방문 기록으로 결정
   - 국소 판단 정확도: Jev 76.5%, 국소 데이터로 학습한 NanoJev 75.0%, 항상 "지나갈 수 있음"이라고 답한 기준선 64.7%
   - 실제 주행: 모든 시스템 3/3 완주 ([MODEL_EDGE_RESULTS](../reference/spatial-src/MODEL_EDGE_RESULTS_nanojev.md))
   - 다만 항상 0.5를 주는 가짜 지각도 3/3 완주. 성능 대부분이 탐색 코드에서 나왔다는 뜻
3. ASCII vs 명시적 좌표, 2×2 비교 ([navigation v3 보고서](../reference/spatial-src/navigation_v3_report_nanojev_zh.md), [프로토콜](../reference/spatial-src/navigation_v3_protocol_nanojev_zh.md))
   - ASCII: 지도만, 좌표·후보 목적지 없음
   - coords: 명시적 좌표 + 인덱스 + 합법적인 다음 칸
   - 같은 지도·같은 학습 조건에서 표현만 다름 (Qwen3-0.6B 기반, seed 1개)
   - coords가 greedy 완주율을 test +55%p, 처음 보는 지도(OOD) +30%p 올림
   - 가장 좋은 모델(coords, 여러 시작점) greedy 완주율: test 90%, OOD 55%
   - 무작위 정책(OOD 70%)과의 완주율 차이는 유의하지 않음. 경로 효율만 확실히 개선 (0.62 vs 0.11)
   - 실패 분석 문서: 한 걸음씩 평가한 정확도가 높아도 실제 주행에서는 같은 칸을 맴도는 문제가 생김

typesafe-mario: 마리오 주변 국소 격자(`#` 벽, `.` 빈칸, `E` 적, `M` 마리오)를 만들어 두고도 모델 입력에서는 뺐다. 대신 물체 중심 JSON(적 위치·접촉 시점·점프 마감)을 넣고, 격자는 디버그 화면용으로만 남김.

#### 이미지 — 게임 데이터로 학습한 모델에서만 사례가 있음

| 사례 | 입력 | 선택지 | 학습 | 결과 |
|---|---|---|---|---|
| [PlayJev](https://github.com/OmniJev/PlayJev) | 게임 화면 1프레임 (448px JPEG, 프레임 누적 없음). 게임 이름은 안 줌 | 게임별 행동 2~7개. 순서는 매번 섞음 | Qwen3.5-0.8B-Base 전체 미세조정. 게임 내부 상태로 탐색 알고리즘(BFS·A*·expectimax)이 정답 생성 → 모방 학습 + DAgger 3라운드. 216만 결정 | 브라우저 게임 10종. 무작위 대비 탐색 정답의 몇 %를 따라잡았는지: Sokoban 1.00, Snake 0.90, Pacman 0.56, 평균 0.57. H200에서 43ms/수 |
| [Valen](https://github.com/Valen-Team/Valen) Sokoban 외 4종 | 타일로 그린 PNG (44px/칸) + 범례·규칙 텍스트 | {Up, Down, Left, Right}, 순서 섞음 | Qwen3.5 + Mixer head. 정답 = 역방향 BFS로 구한 최적 행동들에 확률을 균등 분배. 3만 장 | 데모 영상만 (Sokoban 13수 최적 등). 게임 수치는 미공개 |
| [Jev 1.14 preview](https://www.theaiautomators.com/jev-image-questions-screenshot-automation/) | 이미지 입력 (베타, 별도 헤더 필요) + `box` 질문 타입 | `box`는 영역 좌표를 반환 | — | 게임 사례는 못 찾음. box는 "못 찾음" 답이 없어서 존재 여부 질문을 따로 해야 함 |

Valen의 요청 형식 ([dataset.py 원문](../reference/spatial-src/sokoban_dataset_valen.py)):

```python
{"state": {"messages": [{"role": "user", "content": [
    {"type": "text", "text": "Legend: dark walls, light floor, green rings are goals, crossed squares are boxes, and the round face is the player. ... Move one cell up, down, left or right. ..."},
    {"type": "image_url", "image_url": {"url": "level.png"}}]}]},
 "questions": {"next_action": {"type": "choice",
    "instructions": "Which action should you take next?",
    "criteria": {"left": "Left", "up": "Up", "right": "Right", "down": "Down"}}}}
```

- 렌더러는 격자를 단색 타일로 그린다 (벽·바닥·목표·상자·플레이어). 실제 게임 화면이 아니라 판독하기 쉽게 만든 그림
- 학습 없이 이미지를 넣고 잘 플레이한 System One 사례는 못 찾음

#### 위치를 출력으로 받는 방법 — GUI-Decisions

- [GUI-Decisions](https://github.com/infinitylogesh/GUI-Decisions): 좌표를 축마다 256칸으로 나누고 각 칸을 선택지처럼 읽는다
  - 출력 틀: `action: ___ x: ___ y: ___ ...` 각 빈칸에서 해당 라벨들의 확률분포만 읽음 (생성 없음)
  - 가장 높은 칸 ±2 이웃으로 보정 → (k + 0.5) / 256 × 화면 크기
  - JSON을 생성시키는 것보다 약 3배 빠름 (Gemma 4 31B 146ms vs 470~550ms)
- 상하좌우 같은 이산 행동이 아니라 연속 위치·벡터가 필요할 때 참고할 방식

## 해석 — NPC 엔진에 적용

- 학습 없이 쓸 거라면 4·5·6·8번 조합이 사례들의 주류다.
  - 자기중심(NPC 기준) 상대 위치를 쓴다. 절대 좌표만 주지 않는다.
  - 숫자와 구간 단어를 같이 준다 (doom-jev 방식).
  - 좌표계·부호 규약을 state에 글로 넣는다.
  - 경로·막힘·거리 변화는 코드가 계산해 선택지 설명에 넣는다.
- 격자 NPC라면 상하좌우 선택지에 다음을 넣는 형태가 바로 적용된다 (Snake 방식):
  - 이동 후 좌표
  - 이동 후 플레이어·자극원까지 거리 (가까워지나 멀어지나)
  - 이동 후 갈 수 있는 칸 수, 막다른 길 여부
  - 벽·장애물로 못 가는 방향은 선택지에서 제외
- 전체 지도 ASCII(2번)는 넣되, 판단 근거로 기대하지 않는 게 안전하다. 사례 중 지도만으로 잘한 경우가 없다.
- 국소 창(3번)은 시야 제한 NPC(보이는 범위만 반응)를 만들 때 맞다.
- bbox(1번)처럼 가공을 덜 하려면 미세조정이 필요할 가능성이 높다.
- 격자·이미지 직접 입력 정리:
  - 학습 없이: 전체 격자 → 바로 행동 고르기는 실패 (NanoJev 0/3). 국소 격자 + "이 방향 지나갈 수 있나" 같은 작은 질문 + 코드 플래너는 동작
  - 학습하면: 이미지만으로도 됨 (PlayJev 0.8B, Valen). 정답은 게임 내부 상태로 탐색 알고리즘이 만들어 줌 → 우리 격자 월드에서도 BFS 등으로 정답을 자동 생성할 수 있음
  - 같은 격자라도 명시적 좌표와 합법적인 다음 칸을 같이 주면 크게 좋아짐 (NanoJev +30~55%p)
- 실험 순서 제안: ① 국소 격자 + 좌표 텍스트로 학습 없이 기준선 측정 → ② BFS 정답으로 Laya 미세조정 → ③ 같은 상태를 타일 이미지로 그려 이미지 모델(Valen류)과 비교

## 남은 질문

- 표현 방식만 바꾼 비교는 NanoJev(ASCII vs 좌표) 하나뿐. 학습 seed 1개, 지도 40장이라 근거가 약함. 나머지 효과는 사례별 시행착오 기반
- 이미지 vs 텍스트를 같은 게임에서 비교한 실험은 못 찾음
- PlayJev 수치는 README 자체 보고. 요청 형식(`playjev/model.py`)은 확인 못 함
- 격자 ASCII를 System One 모델이 실제로 얼마나 읽는지 (Laya·Jev 모두 미측정)
- 여러 자극원(플레이어, 소리, 아이템)이 동시에 있을 때 우선순위를 state에 넣을지, 질문을 나눌지

## 출처

- 원문 소스: [spatial-src/](../reference/spatial-src/)
  - [prompt_typesafe-snake.ts](../reference/spatial-src/prompt_typesafe-snake.ts), [analysis_typesafe-snake.ts](../reference/spatial-src/analysis_typesafe-snake.ts) — [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake)
  - [unified_grid_envs_nanojev.py](../reference/spatial-src/unified_grid_envs_nanojev.py), [evaluate_composed_maze_nanojev.py](../reference/spatial-src/evaluate_composed_maze_nanojev.py), [unified_doom_env_nanojev.py](../reference/spatial-src/unified_doom_env_nanojev.py) — [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev)
  - [doom_agent_jev-plays-doom.py](../reference/spatial-src/doom_agent_jev-plays-doom.py) — [tirukovelamanoj/jev-plays-doom](https://github.com/tirukovelamanoj/jev-plays-doom)
  - [observe_doom-war.py](../reference/spatial-src/observe_doom-war.py) — [rythmn1111/doom-war](https://github.com/rythmn1111/doom-war)
  - [state_serializer_doom-jev.py](../reference/spatial-src/state_serializer_doom-jev.py) — [AmoghCreator/doom-jev](https://github.com/AmoghCreator/doom-jev)
  - NanoJev 비교 실험: [ATOMIC_PLANNING](../reference/spatial-src/ATOMIC_PLANNING_nanojev.md), [MODEL_EDGE_RESULTS](../reference/spatial-src/MODEL_EDGE_RESULTS_nanojev.md), [DEVELOPMENT_RESULTS](../reference/spatial-src/DEVELOPMENT_RESULTS_nanojev.md), [navigation v3 보고서](../reference/spatial-src/navigation_v3_report_nanojev_zh.md)
  - [sokoban_render_valen.py](../reference/spatial-src/sokoban_render_valen.py), [sokoban_dataset_valen.py](../reference/spatial-src/sokoban_dataset_valen.py) — [Valen-Team/Valen](https://github.com/Valen-Team/Valen)
- README로만 확인: [PlayJev](https://github.com/OmniJev/PlayJev), [GUI-Decisions](https://github.com/infinitylogesh/GUI-Decisions), [typesafe-mario](https://github.com/fhshaik/typesafe-mario), [Jev 1.14 이미지 입력 기사](https://www.theaiautomators.com/jev-image-questions-screenshot-automation/), [awesome-system-one](https://github.com/andyrewlee/awesome-system-one)
- 글로만 확인: [blocks.ai 블로그](https://blocks.ai/blog/jev-open-model-doom), [CLM T-Rex 예제](https://github.com/Contrastive-LM/CLM/tree/main/examples/t_rex)

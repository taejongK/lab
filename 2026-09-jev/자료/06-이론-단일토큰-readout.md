# 06. 단일토큰 readout의 이론적 배경

[baseline-qwen3-readout.ipynb](../baseline-qwen3-readout.ipynb)가 무슨 원리로 도는지,
그리고 그 원리가 **Jev와 어디서 갈라질 수밖에 없는지**를 정리한다.

한 줄 요약: **readout은 "제약 사건에 대한 베이즈 조건화"이고, 그 조건화는 학습된 적이 없다.**
이 문장의 앞부분이 왜 잘 되는지를, 뒷부분이 왜 위험한지를 설명한다.

---

## 1. 로짓이란 무엇인가

트랜스포머는 위치 $t$에서 은닉상태 $h_t \in \mathbb{R}^d$를 낸다.
LM head $W \in \mathbb{R}^{|V| \times d}$가 이걸 vocab 크기의 로짓 벡터로 바꾼다.

$$z_t = W h_t, \qquad p(x_{t+1} = v \mid x_{\le t}) = \frac{e^{z_{t,v}}}{\sum_{u \in V} e^{z_{t,u}}}$$

중요한 건 **$z_t$가 벡터 하나**라는 것이다. forward 한 번이면 vocab 전체(~15만 차원)에 대한
점수가 **동시에** 손에 들어온다. 그 다음은 전부 인덱싱이다.

일반적인 생성이 느린 건 이 forward가 느려서가 아니라, 토큰을 하나 뽑아 다시 입력에 붙이고
forward를 **또** 하는 루프 때문이다. 우리는 그 루프를 아예 안 돈다.
`Answer:` 다음 위치의 $z_t$ 한 장이 곧 답이기 때문이다.

> 노트북에서 `model.generate()`가 한 번도 안 나오고 `model(**enc)`만 나오는 이유.

## 2. 마스킹 = 베이즈 조건화

후보 집합을 $S \subset V$라 하자 (예: `{" billing", " technical", " sales"}`).
사건 $A = \{x_{t+1} \in S\}$에 대한 조건부 분포는 정의상

$$p(v \mid x_{\le t}, A) = \frac{p(v \mid x_{\le t})}{\sum_{u \in S} p(u \mid x_{\le t})}, \quad v \in S$$

그리고 코드 한 줄 `softmax(z[S])`가 계산하는 건

$$\frac{e^{z_v}}{\sum_{u \in S} e^{z_u}}
= \frac{e^{z_v}/Z}{\sum_{u \in S} e^{z_u}/Z}
= \frac{p(v)}{p(A)}$$

**정확히 같다.** 분모의 정규화상수 $Z$가 소거되므로 softmax를 vocab 전체에 돌릴 필요조차 없다.

### 세 가지 따름정리

**(a) 타입 안전성은 공짜가 아니라 정의다.**
$S$ 밖의 값이 나올 경로가 수식에 존재하지 않는다. 이건 모델이 잘해서가 아니라 우리가
확률공간을 $S$로 제한했기 때문이다. TypeSafe가 각주에서 인정한 것도 이 얘기다 —
*"Schema matching is guaranteed, thus we can confidently add 0% into the plots."*
**측정값이 아니라 항진명제다.**

**(b) $p(A)$가 버려진다.**
조건화는 $p(A)$로 나누고 그 값을 잊는다. 그런데 $p(A)$는
**"답이 내가 준 후보들 중 하나일 것이라고 모델이 믿은 정도"** 다.
후보 집합의 품질에 대한 충분통계량이 바로 이 스칼라인데, 조건화가 그걸 삭제한다.

노트북이 `mass_in_set`을 따로 로깅하는 이유가 이거다:

```python
full = torch.softmax(logits, dim=-1)
mass = full[ids].sum().item()        # = p(A)
```

$p(A) = 0.02$인데 confidence가 0.95라면, 그 0.95는 "95% 확신"이 아니라
**나머지 2% 안에서의 상대 비율**이다. 모델은 전혀 다른 말을 하고 싶었다.

**(c) 그래서 이건 말 그대로 constrained decoding이다.**
문법 기반 constrained decoding(Outlines, XGrammar, GBNF)은 매 스텝 $S_t$를 상태기계로
계산해서 같은 조건화를 반복한다. 후보가 유한 열거집합이면 상태기계의 결정점이 하나뿐인
**퇴화 케이스**가 되고, 그게 우리 구현이다. 다른 물건이 아니라 같은 물건의 가장 단순한 형태다.

## 3. 첫 토큰 근사

후보가 여러 토큰 $o = (o_1, \dots, o_m)$일 때 엄밀한 확률은

$$\log p(o) = \sum_{j=1}^{m} \log p(o_j \mid x_{\le t}, o_{<j})$$

노트북은 대신 $p(o_1)$만 읽는다. 두 가지를 짚어야 한다.

### 무엇을 재고 있는 건가

$p(o_1)$은 $p(o)$가 아니다. **$o_1$으로 시작하는 모든 문자열의 질량 합**이다.

$$p(o_1) = \sum_{\text{$o_1$으로 시작하는 } w} p(w) \;\ge\; p(o)$$

그래도 판별에는 충분하다 — 조건은 하나, **$o \mapsto o_1$이 후보집합 위에서 단사(injective)** 일 것.
`urgent`/`urgency`처럼 첫 토큰이 겹치면 두 후보가 같은 숫자를 읽게 되어 판별이 무너진다.
노트북 셀 6의 충돌 검사가 이 조건을 강제한다.

### 엄밀 계산은 생각보다 싸다 (그러나 함정이 있다)

$o$가 전부 알려져 있으므로 teacher forcing으로 **후보당 forward 1회**, 배치로 묶으면
사실상 1회다. prefix 캐싱까지 쓰면 프롬프트는 공유되고 후보 토큰만 흘리면 된다.
"$k$번 forward라서 비싸다"는 건 과장이다.

진짜 문제는 비용이 아니라 **길이 편향**이다. $\log p(o)$는 토큰 수에 따라 단조 감소하므로
긴 레이블이 구조적으로 불리하다. 표준 대응:

- 길이 정규화: $\frac{1}{m}\log p(o)$
- PMI 정규화: $\log \frac{p(o \mid \text{prompt})}{p(o \mid \text{null prompt})}$

후자는 Holtzman et al. 2021의 **surface form competition** 대응책이다. 같은 개념의 여러
표면형(`"billing"`, `"payment"`, `"invoice"`)이 질량을 나눠 가져서 개념 자체의 확률이
과소평가되는 현상. 후보 이름을 고르는 것이 **모델링 결정**이라는 뜻이기도 하다 —
레이블 워딩을 바꾸면 숫자가 바뀐다.

> 첫 토큰 근사는 이 문제들을 "후보가 첫 글자부터 다르면 어차피 상관없다"로 우회한다.
> 1회 forward를 지키기 위한 **의도적 트레이드오프**이지 근사가 항상 옳아서가 아니다.

## 4. 왜 레이블이 바뀌어도 되는가 — LM head의 구조

이게 BERT 분류 헤드와 갈리는 지점이고, "제너럴한 게 필요하다"는 요구사항의 이론적 핵심이다.

| | 출력층 | 새 레이블 집합 |
|---|---|---|
| BERT 분류기 | $W_c \in \mathbb{R}^{k \times d}$, $k$가 **파라미터 shape** | 행렬 교체 → 재학습 |
| 디코더 LM head | $W \in \mathbb{R}^{\vert V\vert \times d}$, 행 = **토큰 임베딩** | 읽을 행만 바뀜 → 학습 없음 |
| NanoJev식 decision head | 공유 스칼라 $w \in \mathbb{R}^{d}$ + set attention | 후보 수에 무관 → 교체 가능, **단 학습 필수** |

두 경우 모두 로짓은 내적 $z_v = \langle h_t, W_v \rangle$이다. 차이는 $W_v$가 어디서 왔는가다.

- BERT의 $W_c$ 각 행은 **그 태스크를 위해 새로 학습된** 벡터다. 학습 전엔 난수다.
- LM head의 $W_v$ 각 행은 **프리트레이닝 내내 그 토큰의 의미를 학습한** 벡터다.
  `" billing"` 행은 이미 청구/결제 문맥에서 나타나는 방식으로 조형되어 있다.

즉 **LM head는 vocab의 모든 문자열에 대해 미리 학습된 레이블 임베딩 테이블**이다.
후보 집합을 정한다는 건 *이 테이블의 어느 행들과 비교할지*를 고르는 것에 불과하다.
zero-shot이 되는 이유가 여기 있다.

구조적으로는 bi-encoder 검색과 같다 — 쿼리는 state 전체에 대해 문맥화된 $h_t$,
문서는 LM head의 행들. 다만 쿼리 쪽이 지시문과 후보 목록까지 다 읽은 상태라는 점에서
단순 임베딩 유사도보다 훨씬 강하다.

> Jev의 `Choice`가 최대 255개를 받는다는 스펙은 이 관점에서 읽으면 단서가 된다.
> 255개를 의미 레이블로 처리하면 첫 토큰 충돌이 사실상 확실하다.
> 글자/번호 레이블 아니면 성립하지 않는 숫자다.

### 세 번째 길: 후보별 경로 + 공유 스칼라 head

[NanoJev](https://github.com/TianyuCodings/NanoJev)가 쓰는 방식이고, **LM head를 아예 안 쓴다.**
후보 $c$마다 백본을 태운 표현 $g(x, c)$를 얻고, 후보 수에 무관한 스칼라 head로 점수를 낸다:

$$s_c = \langle g(x, c),\, w \rangle, \qquad p = \mathrm{softmax}_{c \in S}(s_c)$$

$w \in \mathbb{R}^d$는 후보 개수와 무관하므로 BERT의 closed-set 문제가 없다. 그리고
**토큰 임베딩에 의존하지 않으므로 첫 토큰 충돌 문제(§3)가 원천적으로 사라진다** —
Jev의 `Choice`가 255개를 받는다는 스펙이 이 구조라면 자연스럽다.
set attention을 얹으면 후보들이 서로를 보면서 "이 중에서 고른다"는 비교가 명시적이 된다.

대가가 둘이다.

**(a) forward 1회가 아니다.** 후보 표현을 따로 태워야 한다. NanoJev README의 계측
*"6 states · 18 questions · 44 candidate paths · 1 backbone forward"* 는 44개 후보 경로를
**배치로 묶어 백본 호출 1회**로 처리했다는 뜻이지, 연산량이 1회분이라는 뜻이 아니다.

**(b) zero-shot이 없다.** 스칼라 head는 난수에서 시작한다. §4에서 본 LM head 방식이
프리트레인된 레이블 임베딩을 공짜로 쓰는 것과 **정확히 반대의 트레이드오프**다.
학습 데이터가 없으면 이 길은 닫혀 있다.

| | zero-shot | 첫 토큰 충돌 | 후보 255개 | forward |
|---|---|---|---|---|
| LM head readout (이 노트북) | ✅ | ⚠️ 검사 필요 | ❌ 사실상 불가 | 1회 |
| decision head (NanoJev) | ❌ 학습 필수 | 해당 없음 | ✅ | 후보 수만큼 (배치) |

## 5. Calibration — 여기가 진짜 쟁점

### 정의

모델이 **calibrated**라는 건, confidence $p$로 낸 예측들을 모아 보면 실제로 $p$의 비율로
맞는다는 뜻이다.

$$\mathbb{P}\big(Y = \hat{y} \;\big|\; \text{conf} = p\big) = p \quad \forall p \in [0,1]$$

경험적 측정이 ECE — confidence를 $B$개 구간으로 나누고

$$\mathrm{ECE} = \sum_{b=1}^{B} \frac{n_b}{n} \Big| \mathrm{acc}(b) - \mathrm{conf}(b) \Big|$$

시각화가 reliability diagram이고, **TypeSafe가 끝내 공개하지 않은 그림**이 정확히 이것이다.
calibration을 핵심 세일즈 포인트로 내세우면서 이걸 안 낸 게 이 조사의 가장 큰 구멍이다
([04-벤치마크-검증.md](04-벤치마크-검증.md)).

정확도와 calibration은 **직교한다.** 항상 "80%"라고 말하며 80% 맞히는 모델은 완벽히
calibrated이면서 쓸모가 없을 수 있고, 95% 정확한데 항상 0.999를 외치는 모델은
정확하지만 calibration이 망가진 것이다. confidence gate를 걸 거라면 후자가 더 위험하다.

### Temperature scaling

$$p_T = \mathrm{softmax}(z / T)$$

파라미터가 스칼라 하나. NLL 최소화로 held-out에서 피팅한다 (Guo et al. 2017,
Platt scaling의 특수형). 성질:

- **$T$는 단조변환이라 argmax를 안 바꾼다 → 정확도 불변.** ECE만 겨냥한 수술이다.
- $T > 1$: 분포를 평탄하게 = 과신 교정. instruction-tuned 모델은 대개 여기 해당
- $T < 1$: 날카롭게 = 과소신 교정

한계도 분명하다. **전역 단조변환**이라 개별 사례의 오calibration이나 순위 오류는 못 고친다.
"모르는 걸 모른다고 아는" 능력을 만들어주지는 않는다. ECE 숫자를 내릴 뿐이다.

### 왜 태스크군별로 따로 잡나

후보 개수 $k$가 다르면 confidence의 의미 자체가 이동한다. 균등분포의 최대확률이 $1/k$라
$k=2$에서의 0.7과 $k=4$에서의 0.7은 다른 사건이다. 게다가 군마다 로짓 스케일이 다르다.
그래서 노트북은 `TEMPS[family]`로 군별 $T$를 잡는다.

### 왜 애초에 miscalibrated인가 — 목적함수 불일치

여기가 이 문서에서 제일 중요한 부분이다.

LM 프리트레이닝은 다음 토큰에 대한 NLL을 최소화한다. NLL은 **proper scoring rule**이라
최소점이 참분포다. 따라서 베이스 모델은 **텍스트에 대해서는** 원리상 calibrated이다.
실제로 프리트레인 베이스 모델이 객관식에서 꽤 좋은 calibration을 보인다는 관측이 있고,
RLHF 이후 그 curve가 무너진다는 것도 (GPT-4 리포트 등에서) 보고됐다.
RLHF의 목적함수는 선호 보상이지 확률의 정직성이 아니기 때문이다.

그런데 우리 문제는 그보다 더 근본적이다:

> **모델은 "텍스트 위의 분포"로 학습됐는데, 우리는 그걸 "결정 위의 분포"로 읽고 있다.**

마스킹 + 재정규화라는 **변환 자체가 한 번도 학습 신호를 받은 적이 없다.**
$p(v \mid A)$가 잘 calibrated이려면 그 조건부 분포에 손실이 걸렸어야 하는데,
프리트레이닝은 $p(v)$에만 손실을 걸었다. 이건 RLHF 유무와 무관한 구조적 간극이다.

**그래서 temperature scaling은 사후 반창고다.** 틀린 층위에서 학습된 분포를 스칼라 하나로
민 것이지, 결정 분포를 제대로 학습시킨 게 아니다.

## 6. 그래서 RLCD는 무엇이어야 하는가

위 논의가 곧 반증 가능한 예측을 준다. RLCD가 실재한다면 **마스크를 통과시켜 학습**했어야 한다.
즉 손실이 마스킹 후 분포 위에 직접 걸려야 한다:

$$\mathcal{L} = \mathbb{E}_{(x, S, y)} \big[ -\log p_\theta(y \mid x, S) \big]$$

여기서 $S$는 **후보 집합들의 분포**에서 뽑힌다 — 다양한 크기, 다양한 레이블 워딩.
proper scoring rule(NLL 또는 Brier)을 결정 위에 직접 걸면 그 분포는 정의상 calibration으로
수렴한다. 이게 "constrained decoding과 다르다"는 주장이 성립할 수 있는 **유일한 형태**다.

> **방증**: NanoJev는 실제로 이 모양으로 학습한다 — README의
> *"observed-event datasets, **CE/Brier training**, paired proper-reward learning"*.
> CE와 Brier는 둘 다 proper scoring rule이고, 그걸 **결정 분포 위에** 걸었다.
> 위 $\mathcal{L}$의 예측과 형태가 일치한다. RLCD가 실재한다면 이 근처일 것이라는
> 간접 증거이지, Jev가 그렇게 했다는 증거는 아니다.

### 검증 가능한 예측 두 개

**예측 1 — $p(A)$가 무의미해진다.**
마스크를 통과시켜 학습하면 $S$ 밖의 질량은 손실에 영향을 주지 않는다. 따라서
`mass_in_set`은 학습 중 아무 압력도 받지 않고, 진단 가치를 잃는다.
→ Jev에서 후보 밖 정답을 탐지할 방법은 **`none_of_the_above`를 실제 후보로 넣는 것뿐**이다.

**예측 2 — 노트북 셀 11이 Jev에서 다르게 나와야 한다.**
정답을 후보에서 제거했을 때:

| | 우리 베이스라인 (마스킹) | RLCD가 진짜라면 |
|---|---|---|
| confidence | 거의 안 떨어짐 (자신있게 지어냄) | **유의하게 하락** |
| `mass_in_set` | 급락 (숨겨졌던 게 드러남) | 측정 불가/무의미 |
| $p(\text{none})$ | 보통 수준 | 상승 |

**confidence가 안 떨어지면 RLCD는 마케팅이다.** 이게 지금까지 설계한 것 중 가장 날카로운
단일 판별 테스트고, 레이블도 거의 필요 없다 (기존 데이터에서 정답만 빼면 됨).

## 7. 정리

| 층위 | 우리 구현 | 이론적 지위 |
|---|---|---|
| 타입 안전 | 확률공간을 $S$로 제한 | **항진명제.** 차별점 아님 |
| 후보 교체 | LM head 행 인덱싱 | 프리트레인 레이블 임베딩 재사용 → zero-shot |
| 1회 forward | 로짓 벡터 한 장 | 디코딩 루프 부재. 첫 토큰 단사성이 조건 |
| 확률 | $p(v)/p(A)$ | **학습된 적 없는 변환.** 여기가 취약점 |
| calibration | 사후 $T$ 피팅 | 반창고. 결정 층위 학습이 아님 |
| Jev의 차별점 주장 | — | 마스크 통과 학습이어야 성립. **미검증** |

`readout`이 잘 도는 이유는 이론적으로 명확하다 — 프리트레인된 레이블 임베딩 위에서의
베이즈 조건화이기 때문이다. **위험한 지점도 똑같이 명확하다** — 그 조건화 자체는 아무도
학습시킨 적이 없고, 우리는 그 결과를 confidence라고 부르며 자동화 게이트를 걸려 하고 있다.

## 참고

- Guo et al. 2017, *On Calibration of Modern Neural Networks* — temperature scaling, ECE
- Holtzman et al. 2021, *Surface Form Competition* — PMI 정규화, 객관식 스코어링 함정
- Willard & Louf 2023, *Efficient Guided Generation for LLMs* — Outlines, FSA 인덱스 사전계산
- Yin et al. 2019, *Benchmarking Zero-shot Text Classification* — NLI 기반 zero-shot (비교군)
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — Qwen3-0.6B + decision head, CE/Brier 학습. 세 번째 길의 실물
- [02-아키텍처-학습.md](02-아키텍처-학습.md) — RLCD 주장과 회의론
- [baseline-qwen3-readout.ipynb](../baseline-qwen3-readout.ipynb) — 이 문서의 구현

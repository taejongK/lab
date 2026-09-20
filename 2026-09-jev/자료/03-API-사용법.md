# 03. API와 사용법

## 엔드포인트

```
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer $TYPESAFE_API_KEY
```

모델 하나당 엔드포인트가 따로 있지 않고, `model` 필드로 라우팅한다.

## 모델 / 한계 / 가격

| 항목 | 값 |
|---|---|
| 현재 모델 | `jev-1.13.0` (별칭 `jev-latest`, `jev-preview`) |
| 입력 가격 | **$0.042 / MTok** ($42 / BTok) |
| 출력 가격 | **무료** (unmetered) |
| 컨텍스트 | 요청당 총 64k 토큰 |
| state 제한 | state + 가장 긴 질문 = 32k 토큰 |
| 입력 타입 | **텍스트만** (이미지/오디오/비디오 불가) |
| 처리량 | 250,000 tok/s |
| RPM | 1,200 req/min (수요에 따라 동적 조정) |
| 언어 | 다국어 지원, 영어에서 최적 |

가격 참고: GPT-5.6 Terra 입력가 $2.00/MTok의 약 1/48.
TypeSafe 본인들도 현재 가격이 **보조금일 수 있다**고 인정했다.

fine-tuning은 없다. 커스터마이즈는 요청 파라미터로 한다 —
고유 데이터는 `state`, 도메인 규칙은 `instructions` / `criteria`.

## 3개 프리미티브

| 프리미티브 | 반환 | 쓰임 |
|---|---|---|
| **Noul** | yes/no 확률 (0~1) | 탐지, 정책 체크, 가드레일 |
| **Choice** | 미리 준 선택지 중 1개 (**최대 255개**) + 전 선택지 확률 | 분류, 라우팅, 인텐트 |
| **Score** | 순서 있는 의미 척도 위 위치 (**2~10 레벨**) + 확률가중 위치 | 심각도, 관련성, 품질 |

셋 다 **전체 확률분포 + confidence(0~1)** 를 함께 준다.
"뭘 생각하는가"와 "얼마나 확신하는가"가 분리되어 나온다는 게 설계 포인트.

## Python SDK

```bash
uv add typesafe-sdk        # 또는 pip install typesafe-sdk
export TYPESAFE_API_KEY=...
```

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "category": Choice(
                instructions="What is this ticket about?",
                criteria={"billing": None, "technical": None, "other": None},
            ),
        },
    )

print(response.choices["category"].choice)
```

## Raw HTTP

```python
import requests

response = requests.post(
    "https://api.typesafe.ai/v1/systemone",
    headers={"Authorization": "Bearer YOUR_KEY"},
    json={
        "model": "jev-latest",
        "state": "Customer emailed twice this week about a failed refund...",
        "questions": {
            "category": {"type": "choice", "options": ["billing", "technical", "sales"]},
            "urgency": {"type": "score", "min": 0, "max": 100},
        },
    },
)
```

> 주의: 위 raw JSON 형태는 2차 자료(DataCamp)에서 온 것이고 SDK 시그니처
> (`criteria` dict 형태)와 모양이 다르다. 실제 키는 공식 docs로 확인 필요.

## 사용 패턴 (중요)

- **독립적인 질문은 한 요청에 묶어서 병렬로 보낸다.** 질문을 추가해도 레이턴시는
  거의 안 늘어난다. 순차 호출은 낭비.
- **한 요청 안의 질문들은 서로 독립적으로 평가된다.** A의 답이 B에 영향을 주지 않는다.
  순차 의존이 필요하면 애플리케이션 코드에서 명시적으로 엮어야 한다.
- **confidence로 자동화 게이트를 건다.** 임계값 이하는 사람/추론모델로 에스컬레이션.
  임계값은 반드시 실제 도메인 데이터로 검증하고 정할 것.
- **state는 구조화된 객체를 선호.** 필드 관계가 명시적이어야 질문이 직접 참조 가능.
- calibration은 correctness 보장이 아니다. 높은 confidence도 틀릴 수 있다.

## 안 되는 것

- 텍스트 생성 전부 (코드, 이메일, 요약, 설명)
- 근거/rationale 제시 → 규제 도메인 감사에 불리
- 사전 정의 안 된 카테고리 출력
- 외부 리서치, 툴 호출
- 다단계 추론

## 출처

- https://docs.typesafe.ai/models
- https://github.com/typesafe-ai/typesafe-sdk-python
- https://www.datacamp.com/blog/system-one-models-jev
- https://gist.github.com/pjburnhill/adf8d28efcad9df037bfdece178ef965

# server

월드 상태·틱 루프, NPC 에이전트(LLM 호출), 프론트에 상태 전달.

- 스택: FastAPI (Python, `uv` 관리)
- LLM: [uzu](https://github.com/trymirai/uzu) Python 바인딩(`uzu==0.6.3`)으로 프로세스 안에서 직접 실행.
- 모델: Qwen 3.5 0.8B — `alibaba:qwen3.5:0.8b:mirai:mirai-m:4` (uzu README 퀵스타트 모델, 첫 실행 시 자동 다운로드).
  - 대안: uzu CLI 서버(`cargo run --release -p cli -- server --model <model>`, OpenAI 호환 API, 기본 `127.0.0.1:8000`)를 따로 띄우고 HTTP로 호출. 이렇게 하면 FastAPI 기본 포트와 겹치니 포트를 바꿔야 한다.
- (보류) gemma-4-e4b로 바꿀 때: 미리 변환된 Gemma 4는 없으므로 lalamo로 변환한다.
  ```bash
  uv run lalamo convert google/gemma-4-E4B-it   # lalamo 저장소에서 실행, 결과는 models/ 폴더
  ```
  `google/gemma-4-E4B-it`는 Hugging Face에서 Gemma 라이선스 동의가 필요할 수 있다 (확인 안 함).
- 실행 방법: (미정)

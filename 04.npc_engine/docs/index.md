# docs

## worklog
날짜별 작업 로그 — [worklog](worklog/)

## plan
기능 설계·계획
- [AI TRPG 캐릭터 엔진 설계](plan/active/2026_11_05_character-engine-design.md) — 현재 방향. 왕 독살 장면을 첫 완료 기준으로 한 엔진 설계
- [구현 계획](plan/active/2026_11_05_character-engine-plan.md) — 파일 구성과 단계

## report
주요 실험 결과·보고서
- [NPC 엔진 동작 원리 (HTML)](report/2026_11_05_game-mechanics.html) — 시간, 인터랙션, 사건 처리, 기억, 계승, 게임 만들기를 게임 동작 관점에서 정리
- [실제 LLM 왕 독살 첫 측정](report/2026_11_05_openrouter-real-run.md) — DeepSeek 5판 측정. 왕 사망 0판, 크레딧 소진으로 5판째 오염
- [외부 자극 반응 NPC 자료 조사](report/2026_10_25_npc-stimulus-literature.md) — 2023-10~2026-10 논문·업계 사례 정리, 설계 축(지각/판단/실행/지연)
- [System One 모델 게임 플레이 사례](report/2026_10_25_system-one-game-play.md) — Jev·Laya류로 Doom/Snake/T-Rex를 플레이할 때 state·질문·행동 매핑 방식
- [공간 정보를 state에 넣는 방법](report/2026_10_25_spatial-state-encoding.md) — 8가지 공간 표현과 시행착오 + 격자(ASCII vs 좌표 비교)·이미지 입력(PlayJev·Valen) 사례
- [ASCII 맵 NPC 엔진 (HTML)](report/2026_10_25_ascii-map-npc-logic.html) — 가능성 평가 실험(로컬 Laya) + 모델은 목표 선택·코드는 BFS 경로로 나눈 틱 로직 설계, 동작 데모

## reference
조사 자료 원본
- [자료 링크 모음](reference/README.md) — 수집한 논문·문서 링크 표
- [arXiv 초록 원문](reference/npc-papers_arxiv-abstracts.md) — 20편 초록 그대로 (수집일 2026-10-25)
- [공간 직렬화 소스 원문](reference/spatial-src/) — typesafe-snake, NanoJev, jev-plays-doom, doom-war, doom-jev, Valen의 state 생성 코드 + NanoJev 비교 실험 문서

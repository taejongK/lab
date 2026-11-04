# NPC Engine

- 질문: 창작자가 세계와 시나리오를 정하면 AI가 게임 마스터와 NPC를 맡아 진행하는 2D TRPG 엔진을 어떻게 만드는가?
- 상태: 진행중
- 시작일: 2026-10-25
- 최종 수정일: 2026-11-05
- 결론: (아직 없음)

## 실행

```
uv run src/playtest.py                  # 규칙·흐름 자동 검사 (가짜 AI, 비용 없음)
uv run src/server.py --fake --debug     # 브라우저에서 조작 확인 (가짜 AI) → http://127.0.0.1:8765
ANTHROPIC_API_KEY=... uv run src/server.py          # 실제 Claude (비용 발생)
ANTHROPIC_API_KEY=... uv run src/playtest.py --real --runs 5   # 품질·비용 측정
```

방향키로 이동, E로 인터랙션, J로 기억 보기. 게임은 `scenarios/`의 시나리오 파일과 도트 데이터로 정의한다.

## 문서

직접 쓴 문서는 `docs/notes/`에, 외부 자료는 `docs/reference/`에 둔다.

| 파일 | 내용 |
|---|---|
| [docs/reference/](docs/reference/) | 외부 자료 링크 모음 |
| [docs/report/2026_10_25_npc-stimulus-literature.md](docs/report/2026_10_25_npc-stimulus-literature.md) | 외부 자극 반응 NPC 최근 3년 자료 조사 |
| [docs/report/2026_10_25_system-one-game-play.md](docs/report/2026_10_25_system-one-game-play.md) | System One 모델로 게임 플레이하는 방식 (state → 상하좌우 선택) |
| [docs/report/2026_10_25_spatial-state-encoding.md](docs/report/2026_10_25_spatial-state-encoding.md) | 공간 정보를 state 텍스트로 넣는 8가지 방식 (사례 소스 기준) |
| [docs/report/2026_10_25_ascii-map-npc-logic.html](docs/report/2026_10_25_ascii-map-npc-logic.html) | ASCII 맵 NPC 엔진 설계 — 가능성 평가 실험 결과와 틱 로직 |
| [docs/plan/active/2026_11_05_character-engine-design.md](docs/plan/active/2026_11_05_character-engine-design.md) | AI TRPG 캐릭터 엔진 설계 (현재 방향, 기존 조사·실험은 전제로 삼지 않음) |
| [docs/plan/active/2026_11_05_character-engine-plan.md](docs/plan/active/2026_11_05_character-engine-plan.md) | 구현 계획 |

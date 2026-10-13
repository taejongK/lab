# frontend

2D 월드 렌더링, 플레이어 입력, 서버와 실시간 통신.

- 스택: HTML5 Canvas 2D + 순수 JS. 빌드 도구·npm 없이 `index.html` 하나로 시작.
- 스타일: 도트 게임. 16×16 타일·캐릭터 스프라이트를 정수배(예: ×3)로 확대하고 `ctx.imageSmoothingEnabled = false`로 픽셀이 뭉개지지 않게 한다.
- 에셋 후보: [Kenney Tiny Town](https://kenney.nl/assets/tiny-town) (16×16, CC0). 걷기 애니메이션·Tiled 맵이 많아지면 Phaser로 옮기는 걸 검토.
- 통신: WebSocket으로 서버에서 월드 상태를 받고 플레이어 입력을 보낸다 .
- 실행 방법: (미정)

"""1단계 스모크: Qwen 3.5 0.8B를 uzu로 받아서 NPC 행동 프롬프트를 몇 번 호출, 지연·형식 확인.

uv run python smoke_llm.py
"""
import asyncio
import json
import time

from uzu import ChatConfig, ChatMessage, ChatReplyConfig, Engine, EngineConfig, Grammar, ReasoningEffort

MODEL = "alibaba:qwen3.5:0.8b:mirai:mirai-m:4"
PLACES = ["plaza", "well", "bakery", "home"]
SCHEMA = json.dumps({
    "type": "object",
    "properties": {"action": {"enum": ["move", "wait"]}, "target": {"enum": PLACES}},
    "required": ["action", "target"],
})
SYSTEM = "You are Mina, a curious villager in a small 2D village. Reply with one JSON object only."
USER = (
    "You are at: plaza. Nearby: Tom. Recent events: Tom said 'The bread at the bakery is fresh today.'\n"
    f"Places: {', '.join(PLACES)}.\n"
    'Choose your next action. Format: {"action": "move" | "wait", "target": <place>}'
)


async def main() -> None:
    engine = await Engine.create(EngineConfig.create())
    model = await engine.model(MODEL)
    assert model is not None, MODEL
    async for u in (await engine.download(model)).iterator():
        print(f"\rdownload {u.progress:.0%}", end="", flush=True)
    print()
    session = await engine.chat(model, ChatConfig.create())

    for grammar in (None, Grammar.JsonSchema(SCHEMA)):
        cfg = ChatReplyConfig.create().with_token_limit(64).with_grammar(grammar)
        for i in range(5):
            msgs = [
                ChatMessage.system().with_text(SYSTEM).with_reasoning_effort(ReasoningEffort.Disabled),
                ChatMessage.user().with_text(USER),
            ]
            await session.reset()  # 세션이 기록을 누적함 → 매 판단은 독립 프롬프트
            t = time.perf_counter()
            replies = await session.reply(msgs, cfg)
            dt = time.perf_counter() - t
            text = replies[-1].message.text if replies else None
            try:
                ok = json.loads(text)["target"] in PLACES
            except Exception:
                ok = False
            print(f"grammar={'schema' if grammar else 'none':6} #{i} {dt:5.2f}s ok={ok} text={text!r}")


asyncio.run(main())

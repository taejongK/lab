"""LLM 호출은 이 모듈에서만. uzu + Qwen 3.5 0.8B."""
import asyncio
import logging

from uzu import ChatConfig, ChatMessage, ChatReplyConfig, Engine, EngineConfig, ReasoningEffort

MODEL = "alibaba:qwen3.5:0.8b:mirai:mirai-m:4"
log = logging.getLogger("uvicorn.error")
_session = None
_lock = asyncio.Lock()  # 모델 인스턴스가 하나 → 호출은 한 번에 하나


async def load() -> None:
    global _session
    engine = await Engine.create(EngineConfig.create())
    model = await engine.model(MODEL)
    assert model is not None, MODEL
    async for _ in (await engine.download(model)).iterator():
        pass
    _session = await engine.chat(model, ChatConfig.create())
    log.info("LLM loaded: %s", MODEL)


async def ask(system: str, user: str) -> str | None:
    """system/user 프롬프트 → 응답 텍스트. 실패하면 None.

    uzu 0.6.3에서 Grammar(JsonSchema/Regex)는 설정해도 무시됨(2026-10-13 확인) → 형식은 프롬프트로만 유도.
    """
    async with _lock:
        try:
            await _session.reset()  # 세션이 기록을 누적함 → 매 판단은 독립 프롬프트
            replies = await _session.reply(
                [
                    ChatMessage.system().with_text(system).with_reasoning_effort(ReasoningEffort.Disabled),
                    ChatMessage.user().with_text(user),
                ],
                ChatReplyConfig.create().with_token_limit(96),
            )
            return replies[-1].message.text if replies else None
        except Exception:
            log.exception("LLM call failed")
            return None

import async_timeout
import asyncio
from fastapi import HTTPException

GENERATION_TIMEOUT_SEC = 60


async def stream_generator(subscription):
    async with async_timeout.timeout(GENERATION_TIMEOUT_SEC):
        try:
            async for event in subscription:
                if "content" in event["choices"][0].delta:
                    current_response = event["choices"][0].delta.content
                    yield "data: " + current_response + "\n\n"
        except asyncio.TimeoutError:
            raise HTTPException(status_code=504, detail="Stream timed out")

import async_timeout
import asyncio
from fastapi import HTTPException

GENERATION_TIMEOUT_SEC = 60


async def stream_generator(subscription):
    async with async_timeout.timeout(GENERATION_TIMEOUT_SEC):
        try:
            async for chunk in subscription:
                yield post_processing(chunk)
        except asyncio.TimeoutError:
            raise HTTPException(status_code=504, detail="Stream timed out")


async def post_processing(chunk):
    print(chunk)
    return chunk

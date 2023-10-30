from fastapi import FastAPI, HTTPException
from starlette.responses import StreamingResponse
import openai

from src.models.inference_request import InferenceRequest
from src.utils import stream_generator
from src.core.config import settings

app = FastAPI()

DEFAULT_SYSTEM_PROMPT = """You are a helpful, respectful and honest Python programmer assistant. 
Generate the best code and answer every question with a code example related to the question."""


@app.post(f"/openai_streaming")
async def openai_streaming(request: InferenceRequest) -> StreamingResponse:
    try:
        subscription = await openai.ChatCompletion.acreate(
            model=request.model_name,
            api_key=settings.OPENAI_API_KEY,
            messages=[
                {
                    "role": "system",
                    "content": DEFAULT_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": request.input_text,
                },
            ],
            stream=True,
            **request.generation_cfg,
        )

        return StreamingResponse(
            stream_generator(subscription), media_type="text/event-stream"
        )
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI call failed: {e}")


import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

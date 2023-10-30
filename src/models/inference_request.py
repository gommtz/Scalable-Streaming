from pydantic import BaseModel
from typing import Optional


class InferenceRequest(BaseModel):
    model_name: Optional[str] = "gpt-4"
    input_text: str
    generation_cfg: Optional[dict] = None

from pydantic import BaseModel
from typing import Optional


class InferenceRequest(BaseModel):
    model_name: str
    input_text: str
    api_key: Optional[str]
    org_id: Optional[str] = None
    generation_cfg: Optional[dict] = None

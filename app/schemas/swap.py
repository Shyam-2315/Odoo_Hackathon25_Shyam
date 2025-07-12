from pydantic import BaseModel
from typing import Literal


class SwapRequest(BaseModel):
    item_id: int
    type: Literal["swap", "redeem"]


class SwapResponse(BaseModel):
    id: int
    item_id: int
    requester_id: int
    type: str
    status: str

    class Config:
        orm_mode = True

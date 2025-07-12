from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class SwapStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    completed = "completed"

class SwapBase(BaseModel):
    item_id: int
    offered_to_id: int

class SwapCreate(SwapBase):
    pass

class SwapOut(SwapBase):
    id: int
    offered_by_id: int
    status: SwapStatus
    timestamp: datetime

    class Config:
        from_attributes = True

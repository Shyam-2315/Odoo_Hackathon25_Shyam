from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ItemStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class ItemBase(BaseModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    size: Optional[str]

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int
    status: ItemStatus
    owner_id: int

    class Config:
        from_attributes = True

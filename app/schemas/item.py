from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: str
    category: str
    size: str
    condition: str
    tags: Optional[str] = None
    image_url: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
    is_available: bool
    status: str
    owner_id: int

    class Config:
        orm_mode = True

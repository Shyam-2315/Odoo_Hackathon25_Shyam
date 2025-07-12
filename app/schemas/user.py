from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    points: int
    is_admin: bool

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str


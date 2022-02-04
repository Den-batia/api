from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemModel(ItemBase):
    title: str
    description: str


class UserBase(BaseModel):
    email: str
    id: UUID


class UserCreate(UserBase):
    password: str


class UserModel(UserBase):
    email: str
    hashed_password: str
    # items: list[ItemModel] = []


class ItemOut(ItemBase):
    user: UserBase


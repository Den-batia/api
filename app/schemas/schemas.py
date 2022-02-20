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
    username: str


class UserCreate(UserBase):
    is_active: bool = False
    password: str


class UserModel(UserBase):
    hashed_password: str
    # items: list[ItemModel] = []


class ItemOut(ItemBase):
    user: UserBase


class TokenData(BaseModel):
    username: str | None = None


class RoleCreate(BaseModel):
    name: str
    descriptions: str

from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemModel(ItemBase):
    id: int
    title: str
    description: str


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserModel(UserBase):
    email: str
    hashed_password: str
    # items: list[ItemModel] = []


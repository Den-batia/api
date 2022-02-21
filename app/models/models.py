import datetime
from typing import Optional, Union
from uuid import UUID, uuid4
from ormar import property_field
import ormar
from db.connection import metadata, database


class MainMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


class Role(ormar.Model):

    class Meta(MainMeta):
        pass

    id: UUID = ormar.UUID(primary_key=True, default=uuid4, uuid_format='string')
    name: str = ormar.String(max_length=50, index=True, unique=True)
    descriptions: str = ormar.String(max_length=100)


class User(ormar.Model):

    class Meta(MainMeta):
        orders_by = ['-username']

    id: UUID = ormar.UUID(primary_key=True, default=uuid4, uuid_format='string')
    username: str = ormar.String(unique=True, max_length=20)
    hashed_password: str = ormar.String(max_length=100)
    is_active: bool = ormar.Boolean(default=False)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    role: Role | None = ormar.ForeignKey(Role, related_name='users')

    @property_field
    def property_field_name(self):
        return f'{self.username} created_at {self.created_at}'


class Item(ormar.Model):

    class Meta(MainMeta):
        pass

    id: UUID = ormar.UUID(primary_key=True, default=uuid4, uuid_format='string')
    title: str = ormar.String(max_length=10)
    description: str | None = ormar.Text(default='')
    user: User | None = ormar.ForeignKey(User, related_name="items")
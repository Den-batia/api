import datetime
from uuid import UUID, uuid4
from ormar import property_field
import ormar
from db.init_bd import MainMeta, metadata


class User(ormar.Model):

    class Meta(MainMeta):
        orders_by = ['-username']

    id: UUID = ormar.UUID(primary_key=True, default=uuid4, uuid_format='string')
    username: str = ormar.String(unique=True, max_length=20)
    hashed_password: str = ormar.String(max_length=100)
    is_active: bool = ormar.Boolean(default=False)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)

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

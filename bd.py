import datetime
from uuid import UUID, uuid4
import sqlalchemy
import databases
from ormar import property_field

from config import DATA_BD
import ormar


# engine = sqlalchemy.create_engine(DATA_BD)
metadata = sqlalchemy.MetaData()
database = databases.Database(DATA_BD)


class MainMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


class User(ormar.Model):

    class Meta(MainMeta):
        orders_by = ['-email']

    id: UUID = ormar.UUID(primary_key=True, default=uuid4, uuid_format='string')
    email: str = ormar.String(unique=True, max_length=20)
    hashed_password: str = ormar.String(max_length=20, nullable=True, )
    is_active: bool = ormar.Boolean(default=False)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)

    @property_field
    def property_field_name(self):
        return f'{self.email}_{self.hashed_password}'


class Item(ormar.Model):

    class Meta(MainMeta):
        pass

    id: UUID = ormar.UUID(primary_key=True, default=uuid4, uuid_format='string')
    title: str = ormar.String(max_length=10)
    description: str = ormar.Text()
    user: User | None = ormar.ForeignKey(User, related_name="items")

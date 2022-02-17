import databases
import sqlalchemy
import ormar
from core import config

metadata = sqlalchemy.MetaData()
database = databases.Database(config.DATA_BD)


class MainMeta(ormar.ModelMeta):
    database = database
    metadata = metadata

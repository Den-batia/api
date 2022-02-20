import databases
import sqlalchemy
from core import config

metadata = sqlalchemy.MetaData()
database = databases.Database(config.DATA_BD)
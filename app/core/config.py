import databases

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

# Config will be read from environment variables and/or ".env" files.
config = Config('.env')

# DEBUG = config('DEBUG', cast=bool, default=False)
DATA_BD = config('EE_DATA_BD', cast=databases.DatabaseURL)
SECRET_KEY = config('SECRET_KEY', cast=str)
ALGORITHM = config('ALGORITHM', cast=str)
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', cast=int)
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings)

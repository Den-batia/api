from starlette.config import Config

config = Config('.env_dev')

DATA_BD = config('EE_DATA_BD', cast=str, default='')
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

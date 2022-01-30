from starlette.config import Config

config = Config('.env_dev')

DATA_BD = config('EE_DATA_BD', cast=str, default='')

from fastapi import FastAPI
import uvicorn
from db.init_bd import database
from fastapi.security import OAuth2PasswordBearer
from routs.endpoints import router


token = OAuth2PasswordBearer(tokenUrl='token')
app = FastAPI()


app.state.database = database

app.include_router(router, prefix="/api/v1/users", tags=["users"])


@app.on_event('startup')
async def startup():
    if not app.state.database.is_connected:
        await app.state.database.connect()


@app.on_event('shutdown')
async def shutdown():
    if not app.state.database.is_connected:
        await app.state.database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="127.0.0.1", reload=True,)
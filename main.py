from fastapi import FastAPI, Depends
import uvicorn
from bd import database, metadata
from config import DATA_BD
from endpoints import router

app = FastAPI()


app.state.database = database

app.include_router(router, prefix="/users", tags=["users"])


@app.on_event('startup')
async def startup():
    if not app.state.database.is_connected:
        await app.state.database.connect()


@app.on_event('shutdown')
async def shutdown():
    if not app.state.database.is_connected:
        await app.state.database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="127.0.0.1", reload=True)
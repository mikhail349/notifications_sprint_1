"""Основной файл сервиса."""
import uvicorn
from fastapi import FastAPI

from src.api.v1.router import router as router_v1
from src.services import broker

app = FastAPI()
app.mount('/api/v1', router_v1)


@app.on_event('startup')
async def startup():
    """Событие запуска FastAPI."""
    await broker.connect()


@app.on_event('shutdown')
async def shutdown():
    """Событие остановки FastAPI."""
    await broker.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

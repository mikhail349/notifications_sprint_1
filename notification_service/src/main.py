"""Основной файл сервиса."""
import uvicorn
from fastapi import FastAPI
from fastapi.routing import Mount

from src.api.v1 import events

v1 = FastAPI()
v1.include_router(events.router)

routes = [
    Mount('/api/v1', v1),
]
app = FastAPI(routes=routes)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

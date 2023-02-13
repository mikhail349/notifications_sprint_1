"""Основной модуль приложения."""
import uvicorn
from fastapi import FastAPI

from src.api.v1.router import router
from src.manager import init_manager

app = FastAPI()
app.mount('/api/v1', router)


@app.on_event('startup')
async def startup():
    """Событие при запуске FastAPi."""
    init_manager()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

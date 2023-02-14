"""Модуль маршрутизатора API версии 1."""
from fastapi import APIRouter, Depends, WebSocket

from src.api.v1.models import Message
from src.auth import login_required, superuser_required
from src.manager import Manager, connect, get_manager
from src.models import User

router = APIRouter()


@router.websocket('/send_messages')
async def send_message(
    websocket: WebSocket,
    manager: Manager = Depends(get_manager),
    user: User = Depends(superuser_required),
):
    """Endpoint для отправки сообщений.

    Args:
        websocket: вебсокет
        manager: менеджер соединений
        user: пользователь

    """
    async with connect(manager, user.username, websocket):
        while True:
            raw_data = await websocket.receive_text()
            msg = Message.parse_raw(raw_data)
            await manager.send(username=msg.username, text=msg.text)


@router.websocket('/receive_messages')
async def receive_messages(
    websocket: WebSocket,
    manager: Manager = Depends(get_manager),
    user: User = Depends(login_required),
):
    """Endpoint для получения сообщений.

    Args:
        websocket: вебсокет
        manager: менеджер соединений
        user: пользователь

    """
    async with connect(manager, user.username, websocket):
        while True:
            await websocket.receive_text()

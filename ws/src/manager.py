"""Модуль менеджера соединений."""
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import Dict, Optional

from fastapi import WebSocket, WebSocketDisconnect


@dataclass
class Manager(object):
    """Класс менеджера соединений."""

    clients: Dict[str, WebSocket] = field(default_factory=dict)

    async def connect(self, username: str, ws: WebSocket) -> None:
        """Установить соединение.

        Args:
            username: имя пользователя
            ws: WebSocket

        """
        self.clients[username] = ws
        await ws.accept()

    def disconnect(self, username: str) -> None:
        """Разорвать соединение.

        Args:
            username: имя пользователя

        """
        del self.clients[username]  # noqa: WPS100

    async def send(self, username: str, text: str) -> None:
        """Отправить сообщение пользователю.

        Args:
            username: имя пользователя
            text: сообщение

        """
        ws = self.clients.get(username)
        if ws is not None:
            await self.clients[username].send_text(text)


manager: Optional[Manager] = None


def init_manager():
    """Инициализировать менеджер."""
    global manager  # noqa: WPS100
    manager = Manager()


def get_manager() -> Manager:
    """Получить менеджер.

    Returns:
        Manager: менеджер

    Raises:
        ValueError: Manager is None
    """
    global manager  # noqa: WPS100
    if manager is None:
        raise ValueError('Manager is not initialized.')
    return manager


@asynccontextmanager
async def connect(manager: Manager, username: str, ws: WebSocket):
    """Контекстный менеджер.

    Используется для подключения и отключения
    пользователя от менеджера соединений.

    Args:
        manager: менеджер соединений
        username: имя пользователя
        ws: вебсокет

    Yields:
        None: None

    """
    await manager.connect(username=username, ws=ws)
    try:
        yield
    except WebSocketDisconnect:
        manager.disconnect(username=username)

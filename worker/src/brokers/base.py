"""Модуль с абстрактным брокером сообщений."""
from abc import ABC, abstractmethod
from typing import Awaitable, Callable

from src.models.notification import Notification

MsgCallback = Callable[[Notification], Awaitable]


class Broker(ABC):
    """Абстрактный класс брокера."""

    @abstractmethod
    async def consume(self, callback: MsgCallback) -> None:
        """Начать слушать очередь.

        Args:
            callback: функция, которая будет вызвана при получении сообщения.

        """

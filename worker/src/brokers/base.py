"""Модуль с абстрактным брокером сообщений."""
from abc import ABC, abstractmethod
from typing import Callable, Dict

MsgCallback = Callable[[Dict], None]


class Broker(ABC):
    """Абстрактный класс брокера."""

    @abstractmethod
    async def consume(self, callback: MsgCallback) -> None:
        """Начать слушать очередь.

        Args:
            callback: функция, которая будет вызвана при получении сообщения.

        """

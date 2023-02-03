"""Модуль с абстрактным брокером сообщений."""
from abc import ABC, abstractmethod

from src.models.base import Notification


class Broker(ABC):
    """Абстрактный класс брокера."""

    @abstractmethod
    async def post(self, notification: Notification) -> None:
        """Отправить сообщение.

        Args:
            notification: инстанс класса `Notification`

        """

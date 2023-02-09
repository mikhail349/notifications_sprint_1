"""Модуль с абстрактным брокером сообщений."""
from abc import ABC, abstractmethod

from src.models.base import Message, PriorityType


class Broker(ABC):
    """Абстрактный класс брокера."""

    @abstractmethod
    async def post(
        self,
        priority: PriorityType,
        message: Message,
    ) -> None:
        """Поставить сообщение в очередь.

        Args:
            priority: приоритет
            message: сообщение

        """

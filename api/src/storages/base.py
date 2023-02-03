"""Модуль абстрактных хранилищ."""
from abc import ABC, abstractmethod
from typing import List

from src.models.base import EventType


class NotificationStorage(ABC):
    """Абстрактный класс хранилища уведомлений."""

    @abstractmethod
    async def get_priorities(self) -> List[str]:
        """Получить список приоритетов.

        Returns:
            `List[str]`: список приоритетов

        """

    @abstractmethod
    async def get_priority(self, event_type: EventType) -> str:
        """Получить приоритет по типу события.

        Args:
            event_type: тип события

        Returns:
            `str`: приоритет

        """

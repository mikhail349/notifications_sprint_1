"""Модуль абстрактных хранилищ."""
from abc import ABC, abstractmethod
from typing import List

from src.models.notification import EventType


class NotificationStorage(ABC):
    """Абстрактный класс хранилища уведомлений."""

    @abstractmethod
    async def get_queues(self) -> List[str]:
        """Получить список очередей.

        Returns:
            `List[str]`: список очередей

        """

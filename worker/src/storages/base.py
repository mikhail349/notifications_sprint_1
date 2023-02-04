"""Модуль абстрактных хранилищ."""
from abc import ABC, abstractmethod
from typing import List

from src.models.notification import EventType
from src.models.notification import DeliveryType
from src.senders.base import Sender


class NotificationStorage(ABC):
    """Абстрактный класс хранилища уведомлений."""

    @abstractmethod
    async def get_queues(self) -> List[str]:
        """Получить список очередей.

        Returns:
            `List[str]`: список очередей

        """

    @abstractmethod
    async def get_sender_plugins(self) -> List[str]:
        """Получить плагины доставщиков

        Returns:
            `List[str]`: список плагинов

        """

    @abstractmethod
    async def get_sender_class(self, delivery_type: DeliveryType) -> str:
        """Получить доставщика

        Args:
            delivery_type: тип доставки `DeliveryType`

        Returns:
            str: класс доставщика

        """
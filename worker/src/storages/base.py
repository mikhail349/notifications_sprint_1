"""Модуль абстрактных хранилищ."""
from abc import ABC, abstractmethod
from typing import List
import uuid

from src.models.notification import DeliveryType, EventType
from src.storages.models.user import User
from src.storages.models.review import Review
from src.storages.models.handler import EventHandler
from src.storages.models.sender import DeliverySender


class DataStorage(ABC):
    """Абстрактный класс хранилища данных."""

    @abstractmethod
    async def get_user(self, username: str) -> User:
        """Получить пользователя.

        Args:
            username: имя пользователя

        Returns:
            User: инстанс пользователя `User`

        """
    
    @abstractmethod
    async def get_review(self, id: uuid.UUID) -> Review:
        """Получить рецензию.

        Args:
            id: ИД рецензии

        Returns:
            Review: инстанс рецензии `Review`

        """       


class NotificationStorage(ABC):
    """Абстрактный класс хранилища уведомлений."""

    @abstractmethod
    async def get_queues(self) -> List[str]:
        """Получить список очередей.

        Returns:
            `List[str]`: список очередей

        """

    @abstractmethod
    async def get_senders(self) -> List[DeliverySender]:
        """Получить список отправителей.

        Returns:
            `List[DeliverySender]`: список отправителей

        """

    @abstractmethod
    async def get_handlers(self) -> List[EventHandler]:
        """Получить список обработчиков событий.

        Returns:
            `List[EventHandler]`: список обработчиков событий

        """

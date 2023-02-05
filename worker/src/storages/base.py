"""Модуль абстрактных хранилищ."""
from abc import ABC, abstractmethod
from typing import List
import uuid

from src.models.notification import DeliveryType, EventType
from src.storages.models.user import User
from src.storages.models.review import Review


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
    async def get_sender_plugins(self) -> List[str]:
        """Получить плагины отправителей.

        Returns:
            `List[str]`: список плагинов

        """

    @abstractmethod
    async def get_handlers(self) -> List[str]:
        """Получить список обработчиков событий.

        Returns:
            `List[str]`: список обработчиков событий

        """

    @abstractmethod
    async def get_handler(self, event_type: EventType) -> List[str]:
        """Получить обработчик по типу события.

        Args:
            event_type: тип события `EventType`

        Returns:
            str: обработчик

        """

    @abstractmethod
    async def get_sender_plugin(self, delivery_type: DeliveryType) -> str:
        """Получить плагин.

        Args:
            delivery_type: тип доставки `DeliveryType`

        Returns:
            str: плагин отправителя

        """

    @abstractmethod
    async def get_template(
        self,
        delivery_type: DeliveryType,
        event_type: EventType,
    ) -> str:
        """Получить шаблон уведомления.

        Args:
            delivery_type: способ доставки
            event_type: тип события

        Returns
            str: шаблон

        """

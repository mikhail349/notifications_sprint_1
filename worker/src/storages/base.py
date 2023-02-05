"""Модуль абстрактных хранилищ."""
import uuid
from abc import ABC, abstractmethod
from typing import List

from src.models.notification import DeliveryType, EventType
from src.storages.models.handler import EventHandler
from src.storages.models.review import Review
from src.storages.models.sender import DeliverySender
from src.storages.models.user import User


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

    @abstractmethod
    async def get_users_by_cohort(self, cohort: str) -> List[User]:
        """Получить список пользователей по когорте.

        Args:
            cohort: название когорты

        Returns:
            List[User]: список пользователей

        """

    @abstractmethod
    async def get_users(self, usernames: List[str]) -> List[User]:
        """Получить пользователей.

        Args:
            usernames: имена пользователей

        Returns:
            List[User]: список пользователей `User`

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

    @abstractmethod
    async def get_template_by_id(self, id: uuid.UUID) -> str:
        """Получить шаблон уведомления по ID.

        Args:
            id: ID шаблона уведомления

        Returns
            str: шаблон

        """

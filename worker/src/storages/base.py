"""Модуль абстрактных хранилищ."""
import enum
import uuid
from abc import ABC, abstractmethod
from typing import Any, List

from src.models.message import DeliveryType, EventType
from src.storages.models.notification import Notification
from src.storages.models.review import Review
from src.storages.models.user import User


class URLType(enum.Enum):
    """Типы URL."""

    CONFIRM_EMAIL_URL = 'confirm_email_url'
    REDIRECT_URL = 'redirect_url'


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
    async def add_notification(self, notification: Notification) -> Any:
        """Добавить уведомление в базу.

        Args:
            notification: уведомление

        Returns:
            Any: ИД уведомления

        """


class ConfigStorage(ABC):
    """Абстрактный класс хранилища настроек."""

    @abstractmethod
    async def get_url(self, url_type: URLType) -> str:
        """Получить URL по ключу.

        Args:
            url_type: ключ URL

        Returns:
            str: URL

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

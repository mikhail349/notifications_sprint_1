"""Модуль хранилища уведомлений MongoDB."""
import enum
from typing import Any

from motor.motor_asyncio import AsyncIOMotorCollection

from src.storages.base import NotificationStorage
from src.storages.models.notification import Notification


class Collection(str, enum.Enum):  # noqa: WPS600
    """Перечисление коллекций."""

    NOTIFICATIONS = 'notifications'


class MongoNotificationStorage(NotificationStorage):
    """Класс хранилища уведомлений MongoDB.

    Args:
        collection: коллекция

    """

    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        """Инициализировать класс хранилища уведомлений MongoDB.

        Args:
            collection: коллекция

        """
        self.collection = collection

    async def add_notification(self, notification: Notification) -> Any:
        document = await self.collection.insert_one(notification.dict())
        return document.inserted_id

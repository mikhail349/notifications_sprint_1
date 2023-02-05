"""Модуль имитации хранилищ."""
from typing import List
import uuid

from src.models.notification import DeliveryType, EventType
from src.storages.base import NotificationStorage, DataStorage
from src.storages.models.user import User
from src.storages.models.review import Review, Movie
from src.storages.models.factory import create_user, create_review
from src.storages.models.handler import EventHandler
from src.storages.models.sender import DeliverySender


class MockedDataStorage(DataStorage):
    """Класс имитации хранилища данных."""

    async def get_user(self, username: str) -> User:
        return create_user(username=username)

    async def get_review(self, id: uuid.UUID) -> Review:
        return create_review(id=id)


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища настроек уведомлений."""

    async def get_queues(self) -> List[str]:
        return ['low_priority', 'high_priority']

    async def get_senders(self) -> List[DeliverySender]:
        return [
            DeliverySender(
                delivery_type=DeliveryType.EMAIL,
                sender_plugin='src.senders.email',
            ),
        ]
    
    async def get_handlers(self) -> List[EventHandler]:
        return [
            EventHandler(
                event_type=EventType.USER_REGISTERED,
                handler_plugin='src.handlers.user',
            ),
        ]

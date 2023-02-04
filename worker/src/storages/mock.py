"""Модуль имитации хранилищ."""
import enum
from typing import List

from src.models.notification import EventType
from src.storages.base import NotificationStorage


class QueueType(enum.Enum):
    """Перечисление очередей."""

    LOW_PRIORITY = 'low_priority'
    HIGH_PRIORITY = 'high_priority'


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища уведомлений."""

    async def get_queues(self) -> List[str]:  # noqa: D102
        return [queue.value for queue in QueueType]

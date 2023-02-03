"""Модуль имитации хранилищ."""
import enum
from typing import List

from src.models.base import EventType
from src.storages.base import NotificationStorage


class PriorityType(enum.Enum):
    """Перечисление приоритетов."""

    LOW_PRIORITY = 'low_priority'  # noqa: WPS115
    HIGH_PRIORITY = 'high_priority'  # noqa: WPS115


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища уведомлений."""

    async def get_priorities(self) -> List[str]:  # noqa: D102
        return [priority.value for priority in PriorityType]

    async def get_priority(  # noqa: D102
        self,
        event_type: EventType,
    ) -> str:
        mapping = {
            EventType.REVIEW_RATED: PriorityType.HIGH_PRIORITY,
            EventType.USER_REGISTERED: PriorityType.HIGH_PRIORITY,
        }
        priority = mapping.get(event_type, PriorityType.LOW_PRIORITY)
        return priority.value

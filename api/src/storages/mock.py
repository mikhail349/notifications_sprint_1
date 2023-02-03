"""Модуль имитации хранилищ."""
from src.models.base import EventType, PriorityType
from src.storages.base import NotificationStorage


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища уведомлений."""

    async def get_priority(  # noqa: D102
        self,
        event_type: EventType,
    ) -> PriorityType:
        mapping = {
            EventType.REVIEW_RATED: PriorityType.HIGH_PRIORITY,
        }
        return mapping.get(event_type, PriorityType.LOW_PRIORITY)

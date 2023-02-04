"""Модуль имитации хранилищ."""
from typing import List

from src.models.notification import DeliveryType
from src.storages.base import NotificationStorage


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища уведомлений."""

    async def get_queues(self) -> List[str]:  # noqa: D102
        return ['low_priority', 'high_priority']

    async def get_sender_plugins(self) -> List[str]:  # noqa: D102
        return ['src.senders.email']

    async def get_sender_plugin(  # noqa: D102
        self,
        delivery_type: DeliveryType,
    ) -> str:
        mapping = {
            DeliveryType.EMAIL: 'src.senders.email',
        }
        return mapping[delivery_type]

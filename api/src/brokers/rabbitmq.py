"""Модуль RabbitMQ."""
import aio_pika

from src.brokers.base import Broker
from src.models.base import Notification
from src.storages.base import NotificationStorage


class RabbitMQ(Broker):
    """Класс RabbitMQ.

    Args:
        exchange: точка обмена `AbstractExchange`
        notification_storage: хранилище уведомлений

    """

    def __init__(
        self,
        exchange: aio_pika.abc.AbstractExchange,
        notification_storage: NotificationStorage,
    ) -> None:
        """Инициализировать класс RabbitMQ.

        Args:
            exchange: точка обмена `AbstractExchange`
            notification_storage: хранилище уведомлений

        """
        self.exchange = exchange
        self.notification_storage = notification_storage

    async def post(self, notification: Notification) -> None:
        """Отправить уведомление в очередь.

        Args:
            notification: инстанс уведомления `Notification`

        """
        priority = (
            await self.notification_storage.get_priority(
                notification.event_type,
            )
        )
        await self._post(priority=priority, payload=notification)

    async def _post(
        self,
        priority: str,
        payload: Notification,
    ) -> None:
        """Вспомогательный метод отправки уведомления.

        Args:
            priority: приоритет
            payload: инстанс класса `Event`

        """
        message = aio_pika.Message(
            body=payload.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(
            message=message,
            routing_key=priority,
        )

"""Модуль RabbitMQ."""
import enum

import aio_pika

from src.brokers.base import Broker
from src.models.base import Notification, EventType, PriorityType
from src.db.base import DataBase



# def get_priority(event_type: EventType) -> PriorityType:
#     """Получить приоритет по типу события.
    
#     Args:
#         event_type: тип события

#     Returns:
#         `PriorityType`: приоритет

#     """
#     mapping = {
#         EventType.REVIEW_RATED: PriorityType.HIGH_PRIORITY
#     }
#     return mapping.get(event_type, PriorityType.LOW_PRIORITY)


class RabbitMQ(Broker):
    """Класс RabbitMQ.

    Args:
        exchange: точка обмена `AbstractExchange`
        db: база данных

    """

    def __init__(
        self,
        exchange: aio_pika.abc.AbstractExchange,
        db: DataBase
    ) -> None:
        """Инициализировать класс RabbitMQ.

        Args:
            exchange: точка обмена `AbstractExchange`
            db: база данных

        """
        self.exchange = exchange
        self.db = db

    async def _post(self, priority: PriorityType, payload: Notification) -> None:
        """Вспомогательный метод отправки уведомления.

        Args:
            routing_key: перечисление `RoutingKey`
            payload: инстанс класса `Event`

        """
        message = aio_pika.Message(
            body=payload.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(
            message=message,
            routing_key=priority.value,
        )
    
    async def post(self, notification: Notification) -> None:
        """Отправить уведомление в очередь.

        Args:
            notification: инстанс уведомления `Notification`

        """
        priority = await self.db.get_priority(notification.event_type)
        await self._post(priority=priority, payload=notification)

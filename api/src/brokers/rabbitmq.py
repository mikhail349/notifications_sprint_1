"""Модуль RabbitMQ."""
import enum

import aio_pika

from src.brokers.base import Broker
# from src.models.base import BaseModel, Event, DeliveryType
from src.models.base import Notification
from src.api.v1.models.base import EventType


class RoutingKey(enum.Enum):
    """Перечисление ключей маршрутизации."""
    LOW_PRIORITY = 'low_priority'  # noqa: WPS115
    HIGH_PRIORITY = 'high_priority'  # noqa: WPS115


class RabbitMQ(Broker):
    """Класс RabbitMQ.

    Args:
        exchange: точка обмена `AbstractExchange`

    """

    def __init__(self, exchange: aio_pika.abc.AbstractExchange) -> None:
        """Инициализировать класс RabbitMQ.

        Args:
            exchange: точка обмена `AbstractExchange`

        """
        self.exchange = exchange

    async def _post(self, routing_key: RoutingKey, payload: Notification) -> None:
        """Отправить сообщение.

        Args:
            routing_key: перечисление `routing_key`
            payload: инстанс класса `Event`
        """
        message = aio_pika.Message(
            body=payload.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(
            message=message,
            routing_key=routing_key.value,
        )
    
    async def post(self, notification: Notification) -> None:
        priority = {
            EventType.REVIEW_RATED: RoutingKey.HIGH_PRIORITY
        }
        await self._post(
            routing_key=priority.get(notification.event_type),
            payload=notification
        )

    # async def post_review_rating(  # noqa: D102
    #     self,
    #     review_rating: ReviewRating,
    # ) -> None:
    #     event = Event(
    #         delivery_type=DeliveryType.EMAIL,

    #         body=review_rating
    #     )
    #     await self.post(RoutingKey.HIGH_PRIORITY, review_rating)

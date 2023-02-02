"""Модуль RabbitMQ."""
import enum

import aio_pika

from src.brokers.base import Broker
from src.models.base import BaseModel
from src.models.review import ReviewRating


class RoutingKey(enum.Enum):
    """Перечисление ключей маршрутизации."""

    REVIEW_RATING = 'review-reporting.v1.rated'  # noqa: WPS115


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

    async def post(self, routing_key: RoutingKey, payload: BaseModel) -> None:
        """Отправить сообщение.

        Args:
            routing_key: перечисление `routing_key`
            payload: инстанс класса `BaseModel`
        """
        message = aio_pika.Message(
            body=payload.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT
        )
        await self.exchange.publish(
            message=message,
            routing_key=routing_key.value,
        )

    async def post_review_rating(  # noqa: D102
        self,
        review_rating: ReviewRating,
    ) -> None:
        await self.post(RoutingKey.REVIEW_RATING, review_rating)

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
        conn: соеднинение RabbitMQ

    """

    def __init__(self, conn: aio_pika.RobustConnection) -> None:
        """Инициализировать класс RabbitMQ.

        Args:
            conn: соеднинение RabbitMQ

        """
        self.conn = conn

    async def disconnect(self) -> None:  # noqa: D102
        self.conn.close()

    async def post(self, routing_key: RoutingKey, payload: BaseModel) -> None:
        """Отправить сообщение.

        Args:
            routing_key: перечисление `routing_key`
            payload: инстанс класса `BaseModel`
        """
        channel = await self.conn.channel()
        queue = await channel.declare_queue(routing_key.value)
        await channel.default_exchange.publish(
            message=aio_pika.Message(payload.json().encode()),
            routing_key=queue.name,
        )

    async def post_review_rating(  # noqa: D102
        self,
        review_rating: ReviewRating,
    ) -> None:
        await self.post(RoutingKey.REVIEW_RATING, review_rating)

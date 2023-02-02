"""Модуль RabbitMQ."""
import enum

import aio_pika

from src.brokers.base import Broker
from src.models.review import ReviewRating
from src.models.base import BaseModel


class RoutingKey(enum.Enum):
    REVIEW_RATING = 'review-reporting.v1.rated'


class RabbitMQ(Broker):
    """Класс RabbitMQ.

    Args:
        conn: соеднинение RabbitMQ

    """

    def __init__(self, conn: aio_pika.RobustConnection) -> None:
        self.conn = conn

    async def disconnect(self) -> None:
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
            routing_key=queue.name
        )

    async def post_review_rating(self, review_rating: ReviewRating) -> None:
        await self.post(RoutingKey.REVIEW_RATING, review_rating)

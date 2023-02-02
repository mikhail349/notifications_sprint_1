"""Модуль RabbitMQ."""
import enum

import aio_pika

from src.brokers.base import Broker


class RoutingKey(enum.Enum):
    """Перечисление ключей маршрутизации."""

    REVIEW_RATING = 'review-reporting.v1.rated'  # noqa: WPS115


class RabbitMQ(Broker):
    """Класс RabbitMQ.

    Args:
        queue: очередь `AbstractQueue`

    """

    def __init__(self, queue: aio_pika.abc.AbstractQueue) -> None:
        """Инициализировать класс RabbitMQ.

        Args:
            queue: очередь `AbstractQueue`

        """
        self.queue = queue

    async def get_message(self) -> None:
        return await super().get_message()

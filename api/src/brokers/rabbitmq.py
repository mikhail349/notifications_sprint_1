"""Модуль RabbitMQ."""
import aio_pika

from src.brokers.base import Broker
from src.models.base import Message, PriorityType


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

    async def post(
        self,
        priority: PriorityType,
        message: Message,
    ) -> None:
        pika_message = aio_pika.Message(
            body=message.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(
            message=pika_message,
            routing_key=priority.value,
        )

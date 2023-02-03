"""Модуль RabbitMQ."""
import enum
import json

import aio_pika

from src.brokers.base import Broker, MsgCallback


class RoutingKey(enum.Enum):
    """Перечисление ключей маршрутизации."""
    LOW_PRIORITY = 'low_priority'  # noqa: WPS115
    HIGH_PRIORITY = 'high_priority'  # noqa: WPS115


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
        self.msg_callback = None

    async def on_message(
        self,
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        """Callback-фунция для получения сообщений.

        Args:
            message: входящее сообщение

        """
        if self.msg_callback is None:
            return
        await self.msg_callback(json.loads(message.body.decode()))

    async def consume(self, callback: MsgCallback) -> None:  # noqa: D102
        self.msg_callback = callback
        await self.queue.consume(self.on_message, no_ack=True)

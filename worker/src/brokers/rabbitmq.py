"""Модуль RabbitMQ."""
import enum
from typing import Optional

import aio_pika

from src.brokers.base import Broker, MsgCallback
from src.models.message import Message


class QueueType(enum.Enum):
    """Перечисление очередей."""

    LOW = 'low'
    HIGH = 'high'


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
        self.msg_callback: Optional[MsgCallback] = None

    async def on_message(
        self,
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        """Callback-функция для получения сообщений.

        Args:
            message: входящее сообщение

        """
        if self.msg_callback is None:
            return

        notification = Message.parse_raw(message.body.decode())
        await self.msg_callback(notification)
        await message.ack()

    async def consume(self, callback: MsgCallback) -> None:
        self.msg_callback = callback
        await self.queue.consume(self.on_message)

"""Модуль имитации брокера сообщений."""
from typing import Optional

from src.brokers.base import Broker, MsgCallback
from src.models.message import Message


class MockedBroker(Broker):
    """Класс имитации брокера сообщений."""

    def __init__(self) -> None:
        """Инициализировать класс."""
        self.msg_callback: Optional[MsgCallback] = None
    
    async def send_message(self, msg: Message):
        """Отправить сообщение.

        Args:
            msg: сообщение

        """
        if self.msg_callback is None:
            return

        await self.msg_callback(msg)

    async def consume(self, callback: MsgCallback) -> None:
        self.msg_callback = callback

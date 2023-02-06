"""Модуль обработчика событий."""
from typing import Dict

from src.brokers.base import Broker
from src.handlers.base import EventHandler
from src.models.notification import DeliveryType, EventType, Notification
from src.senders.base import Sender


class Worker(object):
    """Класс обработчика событий."""

    def __init__(self, broker: Broker) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений

        """
        self.broker = broker
        self.handlers: Dict[EventType, EventHandler] = {}
        self.senders: Dict[DeliveryType, Sender] = {}

    def add_handler(
        self,
        event_type: EventType,
        event_handler: EventHandler,
    ) -> None:
        """Добавить обработчик события.

        Args:
            event_type: тип события
            event_handler: обработчик

        """
        self.handlers[event_type] = event_handler

    def get_handler(self, event_type: EventType) -> EventHandler:
        """Получить обработчик по типу события.

        Args:
            event_type: тип события

        Returns:
            EventHandler: обработчик

        """
        return self.handlers[event_type]

    def add_sender(self, delivery_type: DeliveryType, sender: Sender) -> None:
        """Добавить отправителя.

        Args:
            delivery_type: тип отправки
            sender: отправитель

        """
        self.senders[delivery_type] = sender

    def get_sender(self, delivery_type: DeliveryType) -> Sender:
        """Получить отправителя по типу отправки.

        Args:
            delivery_type: тип отправки

        Returns:
            Sender: отправитель

        """
        return self.senders[delivery_type]

    async def on_message(self, msg: Notification):
        """Событие получения сообщения.

        Args:
            msg: сообщение

        """
        sender = self.get_sender(msg.delivery_type)
        event_handler = self.get_handler(msg.event_type)
        await event_handler.process(msg=msg, sender=sender)
        await event_handler.save_notification(msg)

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)

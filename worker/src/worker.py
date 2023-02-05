"""Модуль обработчика событий."""
import logging
from typing import Dict

from src.brokers.base import Broker
from src.handlers.base import EventHandler
from src.models.notification import DeliveryType, EventType, Notification
from src.senders.base import Sender
from src.templaters.base import Templater


class Worker(object):
    """Класс обработчика событий."""

    def __init__(self, broker: Broker, templater: Templater) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений
            templater: шаблонизатор

        """
        self.logger = logging.getLogger(__name__)

        self.broker = broker
        self.templater = templater
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
        self.logger.info('New message: {0}'.format(msg))

        sender = self.get_sender(msg.delivery_type)
        event_handler = self.get_handler(msg.event_type)
        await event_handler.process(msg=msg, sender=sender)

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)
        self.logger.info('Waiting for messages. To exit press CTRL+C')

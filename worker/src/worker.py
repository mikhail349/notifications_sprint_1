"""Модуль обработчика событий."""
import logging
from typing import Optional, Dict



from src.brokers.base import Broker
from src.models.notification import DeliveryType, EventType, Notification
from src.handlers import factory as handlers_factory
from src.handlers.base import Handler
from src.senders import factory
from src.senders.base import Sender
from src.storages.base import NotificationStorage, DataStorage
from src.storages.models.user import User
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
        self.handlers: Dict[EventType, Handler] = {}
        self.senders: Dict[DeliveryType, Sender] = {}
    
    def add_handler(self, event_type: EventType, handler: Handler) -> None:
        """Добавить обработчик события.

        Args:
            event_type: тип события
            handler: обработчик
        """
        self.handlers[event_type] = handler

    def get_handler(self, event_type: EventType) -> Handler:
        """Получить обработчик по типу события.

        Args:
            event_type: тип события
        
        Returns:
            `Handler`: обработчик
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
        
        Returns
            `Sender`: отправитель

        """
        return self.senders[delivery_type]

    async def on_message(self, msg: Notification):
        """Событие получения сообщения.

        Args:
            msg: сообщение

        """
        self.logger.info('New message: {0}'.format(msg))

        # data getting
        handler = self.get_handler(msg.event_type)
        data = await handler.get_data(msg.body)

        # templating
        template = await self.templater.get_template(
            delivery_type=msg.delivery_type,
            event_type=msg.event_type
        )
        filled_template = self.templater.get_filled_template(
            template=template,
            data=data["payload"]
        )
        
        # sending
        sender = self.get_sender(msg.delivery_type)
        await sender.send(text=filled_template)

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)
        self.logger.info('Waiting for messages. To exit press CTRL+C')

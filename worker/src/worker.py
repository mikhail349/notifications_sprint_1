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

    def __init__(
        self,
        broker: Broker,
        notification_storage: NotificationStorage,
        data_storage: DataStorage,
        templater: Templater,
        name: Optional[str] = None,
    ) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений `Broker`
            notification_storage: хранилище уведомлений
            data_storage: хранилище данных
            templater: шаблонизатор
            name: название воркера

        """
        self.broker = broker
        self.notification_storage = notification_storage
        self.data_storage = data_storage
        self.templater = templater
        self.logger = logging.getLogger(name or __name__)

    async def on_message(self, msg: Notification):
        """Событие получения сообщения.

        Args:
            msg: сообщение

        """
        self.logger.info('New message: {0}'.format(msg))

        handler = await self.get_handler(msg.event_type)
        data = await handler.get_data(msg.body)  
        template = await self.notification_storage.get_template(
            delivery_type=msg.delivery_type,
            event_type=msg.event_type
        )
        filled_template = self.templater.get_filled_template(
            template=template,
            data=data["payload"]
        )
        print("filled_template", filled_template)
        sender = await self.get_sender(msg.delivery_type)
        await sender.send()


    async def get_sender(self, delivery_type: DeliveryType) -> Sender:
        """Получить отправителя.

        Args:
            delivery_type: тип отправки

        Returns:
            Sender: отправитель.

        """
        sender_plugin = (
            await self.notification_storage.get_sender_plugin(delivery_type)
        )
        return factory.create(sender_plugin)
    
    async def get_handler(self, event_type: EventType) -> Handler:
        """Получить обработчик по типу события.

        Args:
            event_type: тип события

        Returns:
            Handler: обработчик.

        """
        handler = await self.notification_storage.get_handler(event_type)
        return handlers_factory.create(handler, storage=self.data_storage)

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)
        self.logger.info('Waiting for messages. To exit press CTRL+C')

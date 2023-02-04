"""Модуль обработчика событий."""
import logging
from typing import Optional, Dict

from src.brokers.base import Broker
from src.models.notification import Notification, DeliveryType
from src.senders.base import Sender
from src.senders import factory
from src.storages.base import NotificationStorage


class Worker(object):
    """Класс обработчика событий.

    Args:
        broker: брокер сообщений `Broker`
        name: название воркера

    """

    def __init__(
        self,
        broker: Broker,
        storage: NotificationStorage,
        name: Optional[str] = None,
    ) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений `Broker`
            name: название воркера

        """
        self.broker = broker
        self.storage = storage
        self.logger = logging.getLogger(name or __name__)

    async def on_message(self, msg: Notification):
        """Событие получения сообщения.

        Args:
            msg: сообщение

        """
        sender_class_str = await self.storage.get_sender_class(msg.delivery_type)
        sender_class = factory.senders.get(sender_class_str)

        if sender_class is None:
            self.logger.error(
                'No sender found for delivery_type: {0}'.format(
                    msg.delivery_type
                )
            )
            return
        
        sender = sender_class()
        await sender.send()
        self.logger.info('New message: {0}'.format(msg))

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)
        self.logger.info('Waiting for messages. To exit press CTRL+C')

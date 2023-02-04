"""Модуль обработчика событий."""
import logging
from typing import Optional

from src.brokers.base import Broker
from src.models.notification import DeliveryType, Notification
from src.senders import factory
from src.senders.base import Sender
from src.storages.base import NotificationStorage


class Worker(object):
    """Класс обработчика событий."""

    def __init__(
        self,
        broker: Broker,
        storage: NotificationStorage,
        name: Optional[str] = None,
    ) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений `Broker`
            storage: хранилище уведомлений
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
        self.logger.info('New message: {0}'.format(msg))

        sender = None
        try:
            sender = self.get_sender(msg.delivery_type)
        except KeyError:
            self.logger.error(
                'No sender found for delivery_type: {0}'.format(
                    msg.delivery_type,
                ),
            )
        if sender is None:
            return
        await sender.send()

    async def get_sender(self, delivery_type: DeliveryType) -> Sender:
        """Получить отправителя.

        Args:
            delivery_type: тип отправки

        Returns:
            Sender: отправитель.

        """
        sender_plugin = (
            await self.storage.get_sender_plugin(delivery_type)
        )
        return factory.create(sender_plugin)

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)
        self.logger.info('Waiting for messages. To exit press CTRL+C')

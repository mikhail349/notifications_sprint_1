"""Модуль обработчика событий."""
import logging

from src.brokers.base import Broker
from src.models.notification import Notification


class Worker(object):
    """Класс обработчика событий.

    Args:
        broker: брокер сообщений `Broker`

    """

    def __init__(self, broker: Broker, name: str = None) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений `Broker`
            name: название воркера

        """
        self.broker = broker
        self.logger = logging.getLogger(name or __name__)

    async def on_message(self, msg: Notification):
        """Событие получения сообщения.

        Args:
            msg: сообщение

        """
        self.logger.info('New message: {0}'.format(msg))

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)
        self.logger.info('Waiting for messages. To exit press CTRL+C')

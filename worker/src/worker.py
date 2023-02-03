"""Модуль обработчика событий."""
import asyncio
import logging
from typing import Dict

from src.brokers.base import Broker

logger = logging.getLogger(__name__)


class Worker(object):
    """Класс обработчика событий.

    Args:
        broker: брокер сообщений `Broker`

    """

    def __init__(self, broker: Broker) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений `Broker`

        """
        self.broker = broker

    async def on_message(self, msg: Dict):
        """Событие полуения сообщения.

        Args:
            msg: сообщение
        """
        logger.info('New message: {0}'.format(msg))

    async def run(self) -> None:
        """Запустить воркер."""
        logger.info('Waiting for messages. To exit press CTRL+C')
        await self.broker.consume(self.on_message)
        await asyncio.Future()

"""Модуль брокера."""
from typing import Union

import aio_pika

from src.brokers.base import Broker
from src.brokers.rabbitmq import RabbitMQ
from src.config.rabbitmq import rabbitmq_settings

broker: Union[Broker, None] = None


async def connect() -> None:
    """Подключиться к брокеру."""
    url = 'amqp://{username}:{password}@{host}:{password}'.format(
        **rabbitmq_settings.dict(),
    )
    connection = await aio_pika.connect_robust(url)
    global broker  # noqa: WPS420
    broker = RabbitMQ(conn=connection)


async def disconnect() -> None:
    """Отключиться от брокера."""
    if broker is not None:
        await broker.disconnect()


def get_broker() -> Union[Broker, None]:
    """Получить брокера.

    Returns:
        `Broker` | `None`: брокер или None
    """
    return broker

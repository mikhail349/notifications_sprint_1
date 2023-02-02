"""Модуль брокера."""
from typing import Union

import aio_pika

from src.config.rabbitmq import rabbitmq_settings
from src.brokers.base import Broker
from src.brokers.rabbitmq import RabbitMQ

broker: Union[Broker, None] = None


async def connect() -> None:
    """Подключиться к брокеру."""
    connection = await aio_pika.connect_robust(
        f'amqp://{rabbitmq_settings.username}:{rabbitmq_settings.password}@'
        f'{rabbitmq_settings.host}:{rabbitmq_settings.port}/',
    )
    global broker
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

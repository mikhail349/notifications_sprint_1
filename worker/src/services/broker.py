"""Модуль брокера."""
from typing import Union

import aio_pika
import backoff

from src.brokers.base import Broker
from src.brokers.rabbitmq import RabbitMQ, RoutingKey
from src.config.rabbitmq import rabbitmq_settings

broker: Union[Broker, None] = None
connection: Union[aio_pika.abc.AbstractConnection, None] = None


@backoff.on_exception(backoff.expo, exception=ConnectionError)
async def get_connection() -> aio_pika.abc.AbstractRobustConnection:
    """Получить соединение с RabbitMQ.

    Returns:
        `AbstractRobustConnection`: соединение RabbitMQ
    """
    url = 'amqp://{username}:{password}@{host}:{port}'.format(
        **rabbitmq_settings.dict(),
    )
    return await aio_pika.connect_robust(url)


async def get_queue(
    connection: aio_pika.abc.AbstractRobustConnection,
    routing_key: RoutingKey
) -> aio_pika.abc.AbstractQueue:
    """Получить очередь RabbitMQ.

    Args:
        connection: соединение RabbitMQ
        routing_key: ключ маршрутизации

    Returns:
        `AbstractQueue`: очередь RabbitMQ
    """
    channel = await connection.channel()
    return await channel.declare_queue(
        name=routing_key.value,
        durable=True,
    )



@backoff.on_exception(backoff.expo, exception=ConnectionError)
async def connect() -> None:
    """Подключиться к брокеру."""
    url = 'amqp://{username}:{password}@{host}:{port}'.format(
        **rabbitmq_settings.dict(),
    )

    global broker, connection  # noqa: WPS420

    connection = await aio_pika.connect_robust(url)
    channel = await connection.channel()
    for routing_key in RoutingKey:
        await channel.declare_queue(
            name=routing_key.value,
            durable=True,
        )

    broker = RabbitMQ(exchange=channel.default_exchange)


async def disconnect() -> None:
    """Отключиться от брокера."""
    if connection is not None:
        await connection.close()


def get_broker() -> Union[Broker, None]:
    """Получить брокера.

    Returns:
        `Broker` | `None`: брокер или None
    """
    return broker

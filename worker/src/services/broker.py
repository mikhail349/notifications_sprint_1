"""Модуль инициализации брокера."""
from typing import List

import aio_pika
import backoff
from pamqp.exceptions import AMQPFrameError

from src.brokers.base import Broker
from src.brokers.rabbitmq import QueueType, RabbitMQ
from src.config.rabbitmq import rabbitmq_settings


async def create_brokers(
    connection: aio_pika.abc.AbstractRobustConnection,
) -> List[Broker]:
    """Создать брокеров.

    Args:
        connection: соединение с RabbitMQ

    Returns:
        List[Broker]: список брокеров

    """
    brokers: List[Broker] = []
    for queue_name in QueueType:
        queue = await get_queue(connection, queue_name.value)
        brokers.append(RabbitMQ(queue, rabbitmq_settings.consumption_delay))
    return brokers


@backoff.on_exception(backoff.expo, exception=(ConnectionError, AMQPFrameError))
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
    routing_key: str,
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
        name=routing_key,
        durable=True,
    )

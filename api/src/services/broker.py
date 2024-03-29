"""Модуль брокера."""
from typing import Union

import aio_pika
import backoff
from pamqp.exceptions import AMQPFrameError

from src.brokers.base import Broker
from src.brokers.rabbitmq import RabbitMQ
from src.config.rabbitmq import rabbitmq_settings
from src.models.base import PriorityType

broker: Union[Broker, None] = None
connection: Union[aio_pika.abc.AbstractConnection, None] = None


@backoff.on_exception(
    backoff.expo,
    exception=(ConnectionError, AMQPFrameError),
)
async def connect() -> None:
    """Подключиться к брокеру."""
    global broker, connection  # noqa: WPS100, WPS420

    connection = await aio_pika.connect_robust(
        'amqp://{username}:{password}@{host}:{port}'.format(
            **rabbitmq_settings.dict(),
        ),
    )
    channel = await connection.channel()
    for priority in PriorityType:
        await channel.declare_queue(
            name=priority.value,
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

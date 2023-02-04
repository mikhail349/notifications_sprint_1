"""Модуль брокера."""
import aio_pika
import backoff

from src.config.rabbitmq import rabbitmq_settings


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

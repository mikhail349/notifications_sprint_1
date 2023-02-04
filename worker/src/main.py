"""Основной файл запуска."""
import asyncio
import logging
from typing import Dict

from aio_pika.abc import AbstractRobustConnection

from src.brokers.rabbitmq import RabbitMQ
from src.models.notification import DeliveryType
from src.senders.base import Sender
from src.senders.email import EmailSender
from src.services.broker import get_connection, get_queue
from src.storages.base import NotificationStorage
from src.storages.mock import MockedNotificationStorage
from src.worker import Worker
from src.senders.loader import setup_plugins


async def create_worker(
    conn: AbstractRobustConnection,
    queue: str,
    storage: NotificationStorage,
) -> Worker:
    """Создать воркер.

    Args:
        conn: соединение с RabbitMQ
        queue: название очереди
        storage: хранилище уведомлений

    Returns:
        Worker: воркер

    """
    queue = await get_queue(conn, queue)
    broker = RabbitMQ(queue)
    worker_name = '{0} worker'.format(queue)
    return Worker(broker, storage=storage, name=worker_name)


async def main():
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    storage = MockedNotificationStorage()
    sender_plugins = await storage.get_sender_plugins()
    setup_plugins(sender_plugins)

    async with await get_connection() as conn:
        for queue in await storage.get_queues():
            worker = await create_worker(conn, queue, storage)
            await worker.run()
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

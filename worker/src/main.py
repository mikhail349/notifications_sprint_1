"""Основной файл запуска."""
import asyncio
import logging

from aio_pika.abc import AbstractRobustConnection

from src.brokers.rabbitmq import RabbitMQ
from src.senders.loader import setup_plugins
from src.services.broker import get_connection, get_queue
from src.storages.base import NotificationStorage, DataStorage
from src.storages.mock import MockedNotificationStorage, MockedDataStorage
from src.templaters.jinja import Jinja2Templater
from src.worker import Worker


async def create_worker(
    conn: AbstractRobustConnection,
    queue: str,
    notification_storage: NotificationStorage,
    data_storage: DataStorage
) -> Worker:
    """Создать воркер.

    Args:
        conn: соединение с RabbitMQ
        queue: название очереди
        notification_storage: хранилище уведомлений
        data_storage: хранилище данных

    Returns:
        Worker: воркер

    """
    queue = await get_queue(conn, queue)
    broker = RabbitMQ(queue)
    worker_name = '{0} worker'.format(queue)
    templater = Jinja2Templater()
    return Worker(
        broker,
        notification_storage=notification_storage,
        data_storage=data_storage,
        templater=templater,
        name=worker_name
    )


async def main():  # noqa: WPS217
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    notification_storage = MockedNotificationStorage()
    data_storage = MockedDataStorage()

    senders = await notification_storage.get_sender_plugins()
    handlers = await notification_storage.get_handlers()
    setup_plugins(senders)
    setup_plugins(handlers)

    async with await get_connection() as conn:
        for queue in await notification_storage.get_queues():
            worker = await create_worker(
                conn,
                queue,
                notification_storage,
                data_storage
            )
            await worker.run()
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

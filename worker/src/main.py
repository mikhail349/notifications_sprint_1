"""Основной файл запуска."""
import asyncio
import logging

from aio_pika.abc import AbstractRobustConnection

from src.brokers.rabbitmq import RabbitMQ
from src.services.broker import get_connection, get_queue
from src.storages.mock import MockedNotificationStorage
from src.worker import Worker


async def create_worker(
    conn: AbstractRobustConnection,
    queue: str,
) -> Worker:
    """Создать воркер.

    Args:
        conn: соединение с RabbitMQ
        queue: название очереди

    Returns:
        Worker: воркер

    """
    queue = await get_queue(conn, queue)
    broker = RabbitMQ(queue)
    worker_name = '{0} worker'.format(queue)
    return Worker(broker, name=worker_name)


async def main():
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    async with await get_connection() as conn:
        storage = MockedNotificationStorage()
        for queue in await storage.get_queues():
            worker = await create_worker(conn, queue)
            await worker.run()
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

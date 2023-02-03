"""Основной файл запуска."""
import asyncio
import logging

from src.brokers.rabbitmq import RabbitMQ
from src.services.broker import RoutingKey, get_connection, get_queue
from src.worker import Worker


async def main():
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    async with await get_connection() as conn:
        queue = await get_queue(conn, RoutingKey.REVIEW_RATING)
        broker = RabbitMQ(queue)
        worker = Worker(broker)
        await worker.run()

if __name__ == '__main__':
    asyncio.run(main())

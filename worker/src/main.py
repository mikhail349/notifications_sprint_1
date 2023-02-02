import asyncio

import aio_pika

from src.services.broker import get_connection, get_queue, RoutingKey
from src.worker import Worker
from src.brokers.rabbitmq import RabbitMQ


async def main():
    async with await get_connection() as conn:
        queue = await get_queue(conn, RoutingKey.REVIEW_RATING)
        broker = RabbitMQ(queue)
        worker = Worker(broker)
        print(worker)
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

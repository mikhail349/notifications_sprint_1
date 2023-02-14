"""Основной файл запуска."""
import asyncio
import logging

from src.services.broker import create_brokers, get_connection
from src.services.worker import create_worker


async def main():
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    async with await get_connection() as conn:
        for broker in await create_brokers(conn):
            worker = await create_worker(broker)
            await worker.run()

        logging.info('Waiting for messages. To exit press CTRL+C')
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

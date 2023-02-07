"""Основной файл запуска."""
import asyncio
import logging


from src.services.broker import get_connection, create_brokers
from src.services.worker import create_worker


async def main():
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    async with await get_connection() as conn:
        for broker in await create_brokers(conn):
            worker = create_worker(broker)
            await worker.run()

        logging.info('Waiting for messages. To exit press CTRL+C')
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

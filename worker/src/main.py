"""Основной файл запуска."""
import asyncio
import logging

from aio_pika.abc import AbstractRobustConnection

from src.brokers.rabbitmq import RabbitMQ
from src.handlers.user import UserHandler
from src.handlers.factory import create as create_handler
from src.models.notification import DeliveryType, EventType
from src.senders.email import EmailSender
from src.senders.loader import load_plugins
from src.senders.factory import create as create_sender
from src.services.broker import get_connection, get_queue
from src.storages.base import NotificationStorage, DataStorage
from src.storages.mock import MockedNotificationStorage, MockedDataStorage
from src.templaters.jinja import Jinja2Templater
from src.worker import Worker


async def main():  # noqa: WPS217
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    notification_storage = MockedNotificationStorage()
    data_storage = MockedDataStorage()
    templater = Jinja2Templater()

    delivery_senders = await notification_storage.get_senders()
    event_handlers = await notification_storage.get_handlers()
    load_plugins([delivery_sender.sender_plugin for delivery_sender in delivery_senders])
    load_plugins([event_handler.handler_plugin for event_handler in event_handlers])

    async with await get_connection() as conn:
        for queue in await notification_storage.get_queues():
            broker = RabbitMQ(await get_queue(conn, queue))
            worker = Worker(
                broker=broker,
                templater=templater
            )
            for event_handler in event_handlers:
                worker.add_handler(
                    event_type=event_handler.event_type,
                    handler=create_handler(
                        event_handler.handler_plugin,
                        storage=data_storage
                    )
                )
            for delivery_sender in delivery_senders:
                worker.add_sender(
                    delivery_type=delivery_sender.delivery_type,
                    sender=create_sender(
                        delivery_sender.sender_plugin
                    )
                )

            await worker.run()
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

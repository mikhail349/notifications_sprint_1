"""Основной файл запуска."""
import asyncio
import logging

from src.brokers.rabbitmq import QueueType, RabbitMQ
from src.handlers.admin import AdminHandler
from src.handlers.review import ReviewHandler
from src.handlers.user import UserHandler
from src.models.message import DeliveryType, EventType
from src.senders.email import EmailSender
from src.senders.sms import SMSSender
from src.senders.websocket import WebsocketSender
from src.services.broker import get_connection, get_queue
from src.services.data_storage import create_data_storage
from src.services.notification_storage import create_notification_storage
from src.services.template_storage import create_template_storage
from src.services.templater import create_templater
from src.services.worker import Worker


def init_handlers(worker: Worker):
    """Инициализировать обработчиков событий.

    Args:
        worker: Воркер

    """
    notification_storage = create_notification_storage()
    data_storage = create_data_storage()
    template_storage = create_template_storage()
    templater = create_templater()

    worker.add_handler(
        EventType.USER_REGISTERED,
        UserHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            template_storage=template_storage,
            templater=templater,
        ),
    )
    worker.add_handler(
        EventType.REVIEW_RATED,
        ReviewHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            template_storage=template_storage,
            templater=templater,
        ),
    )
    worker.add_handler(
        EventType.ADMIN,
        AdminHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            template_storage=template_storage,
            templater=templater,
        ),
    )


def init_senders(worker: Worker):
    """Инициализировать отправителей.

    Args:
        worker: Воркер

    """
    worker.add_sender(DeliveryType.EMAIL, EmailSender())
    worker.add_sender(DeliveryType.SMS, SMSSender())
    worker.add_sender(DeliveryType.WEB_SOCKET, WebsocketSender())


async def main():
    """Основная функция."""
    logging.basicConfig(level=logging.INFO)

    async with await get_connection() as conn:
        for queue_name in QueueType:
            queue = await get_queue(conn, queue_name.value)
            broker = RabbitMQ(queue)

            worker = Worker(broker=broker)
            init_handlers(worker)
            init_senders(worker)
            await worker.run()

        logging.info('Waiting for messages. To exit press CTRL+C')
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

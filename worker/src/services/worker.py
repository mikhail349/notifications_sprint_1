"""Модуль инициализации обработчика событий."""
from src.brokers.base import Broker
from src.handlers.admin import AdminHandler
from src.handlers.review import ReviewHandler
from src.handlers.user import UserRegisteredHandler
from src.models.message import DeliveryType, EventType
from src.services.config_storage import create_config_storage
from src.services.data_storage import create_data_storage
from src.services.email_sender import create_email_sender
from src.services.notification_storage import create_notification_storage
from src.services.templater import create_templater
from src.services.url_shortener import create_url_shortener
from src.services.ws_sender import create_ws_sender
from src.worker import Worker


async def init_worker(worker: Worker):
    """Инициализировать обработчиков событий и отправителей.

    Args:
        worker: Воркер

    """
    notification_storage = create_notification_storage()
    data_storage = create_data_storage()
    config_storage = create_config_storage()
    templater = create_templater()
    url_shortener = create_url_shortener()

    worker.add_handler(
        EventType.USER_REGISTERED,
        UserRegisteredHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=config_storage,
            templater=templater,
            url_shortener=url_shortener,
        ),
    )
    worker.add_handler(
        EventType.REVIEW_RATED,
        ReviewHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=config_storage,
            templater=templater,
        ),
    )
    worker.add_handler(
        EventType.ADMIN,
        AdminHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=config_storage,
            templater=templater,
        ),
    )

    worker.add_sender(DeliveryType.EMAIL, create_email_sender())
    worker.add_sender(
        DeliveryType.WEB_SOCKET,
        await create_ws_sender(data_storage=data_storage),
    )


async def create_worker(broker: Broker) -> Worker:
    """Создать воркер.

    Args:
        broker: брокер сообщений

    Returns:
        Worker: воркер

    """
    worker = Worker(broker=broker)
    await init_worker(worker)
    return worker

"""Модуль обработчика событий."""
from typing import Dict

from src.brokers.base import Broker
from src.handlers.admin import AdminHandler
from src.handlers.base import EventHandler
from src.handlers.review import ReviewHandler
from src.handlers.user import UserRegisteredHandler
from src.models.message import DeliveryType, EventType, Message
from src.senders.base import Sender
from src.services.config_storage import create_config_storage
from src.services.data_storage import create_data_storage
from src.services.email_sender import create_email_sender
from src.services.notification_storage import create_notification_storage
from src.services.templater import create_templater
from src.services.url_shortener import create_url_shortener
from src.services.ws_sender import create_ws_sender
from src.storages.models.notification import Status


class Worker(object):
    """Класс обработчика событий."""

    def __init__(self, broker: Broker) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений

        """
        self.broker = broker
        self.handlers: Dict[EventType, EventHandler] = {}
        self.senders: Dict[DeliveryType, Sender] = {}

    def add_handler(
        self,
        event_type: EventType,
        event_handler: EventHandler,
    ) -> None:
        """Добавить обработчик события.

        Args:
            event_type: тип события
            event_handler: обработчик

        """
        self.handlers[event_type] = event_handler

    def get_handler(self, event_type: EventType) -> EventHandler:
        """Получить обработчик по типу события.

        Args:
            event_type: тип события

        Returns:
            EventHandler: обработчик

        """
        return self.handlers[event_type]

    def add_sender(self, delivery_type: DeliveryType, sender: Sender) -> None:
        """Добавить отправителя.

        Args:
            delivery_type: тип отправки
            sender: отправитель

        """
        self.senders[delivery_type] = sender

    def get_sender(self, delivery_type: DeliveryType) -> Sender:
        """Получить отправителя по типу отправки.

        Args:
            delivery_type: тип отправки

        Returns:
            Sender: отправитель

        """
        return self.senders[delivery_type]

    async def on_message(self, msg: Message):
        """Событие получения сообщения.

        Args:
            msg: сообщение

        """
        sender = self.get_sender(msg.delivery_type)
        event_handler = self.get_handler(msg.event_type)
        try:
            await event_handler.process(msg=msg, sender=sender)
        except Exception as exc:
            await event_handler.save_message(
                msg=msg,
                status=Status.ERROR,
                comments=str(exc),
            )
        else:
            await event_handler.save_message(msg=msg, status=Status.SUCCESS)

    async def run(self) -> None:
        """Запустить воркер."""
        await self.broker.consume(self.on_message)


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

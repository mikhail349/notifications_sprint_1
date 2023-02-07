"""Модуль абстраткного обработчика событий."""
import datetime
from abc import ABC, abstractmethod
from typing import Any, Optional

from src.models.message import Message
from src.senders.base import Sender
from src.storages.base import DataStorage, NotificationStorage, TemplateStorage
from src.storages.models.notification import Notification, Status
from src.templaters.base import Templater


class EventHandler(ABC):
    """Абстрактный класс обработчика событий."""

    def __init__(
        self,
        data_storage: DataStorage,
        notification_storage: NotificationStorage,
        template_storage: TemplateStorage,
        templater: Templater,
    ) -> None:
        """Инициализировать обработчик событий.

        Args:
            data_storage: хранилище данных
            notification_storage: хранилище уведомлений
            template_storage: хранилище шаблонов
            templater: шаблнизатор

        """
        self.data_storage = data_storage
        self.notification_storage = notification_storage
        self.template_storage = template_storage
        self.templater = templater

    @abstractmethod
    async def process(
        self,
        msg: Message,
        sender: Sender,
    ) -> None:
        """Обработать сообщение.

        Args:
            msg: сообщение
            sender: отпрвитель

        """

    async def save_message(
        self,
        msg: Message,
        status: Status,
        comments: Optional[str] = None,
    ) -> Any:
        """Сохранить сообщение в БД.

        Args:
            msg: сообщение
            status: статус отправки
            comments: комментарий отправки

        Returns:
            Any: ИД созданного уведомления

        """
        notification = Notification(
            delivery_type=msg.delivery_type,
            event_type=msg.event_type,
            body=msg.body,
            attempted_at=datetime.datetime.now(),
            status=status,
            comments=comments,
        )
        return await self.notification_storage.add_notification(notification)

"""Модуль абстраткного обработчика событий."""
from abc import ABC, abstractmethod
from typing import Any

from src.models.notification import Notification
from src.senders.base import Sender
from src.storages.base import DataStorage, NotificationStorage
from src.templaters.base import Templater


class EventHandler(ABC):
    """Абстрактный класс обработчика событий."""

    def __init__(
        self,
        data_storage: DataStorage,
        notification_storage: NotificationStorage,
        templater: Templater,
    ) -> None:
        """Инициализировать обработчик событий.

        Args:
            data_storage: хранилище данных
            notification_storage: хранилище уведомлений
            templater: шаблнизатор

        """
        self.data_storage = data_storage
        self.notification_storage = notification_storage
        self.templater = templater

    @abstractmethod
    async def process(
        self,
        msg: Notification,
        sender: Sender,
    ) -> None:
        """Обработать событие.

        Args:
            msg: уведомление
            sender: отпрвитель

        """

    async def save_notification(self, notification: Notification) -> Any:
        """Сохранить уведомление в БД.

        Args:
            notification: уведомление

        Returns:
            Any: ИД созданного уведомления

        """
        return await self.notification_storage.add_notification(notification)

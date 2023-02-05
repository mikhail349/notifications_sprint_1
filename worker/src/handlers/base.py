from abc import ABC, abstractmethod
from typing import Dict

from src.models.notification import Notification
from src.storages.base import DataStorage


class Handler(ABC):
    """Абстрактный класс обработчика событий."""

    def __init__(self, storage: DataStorage) -> None:
        self.storage = storage

    @abstractmethod
    async def get_data(self, msg_body: Dict) -> Dict:
        """Получить данные для события.

        Args:
            msg_body: тело сообщения

        Returns:
            `Dict`: данные

        """

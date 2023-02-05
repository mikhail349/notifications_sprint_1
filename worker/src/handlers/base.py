from abc import ABC, abstractmethod
from typing import Dict

from src.models.notification import Notification


class Handler(ABC):
    """Абстрактный класс обработчика событий."""

    @abstractmethod
    async def get_data(self, msg_body: Dict) -> Dict:
        """Получить данные для события.

        Args:
            msg_body: тело сообщения

        Returns:
            `Dict`: данные

        """

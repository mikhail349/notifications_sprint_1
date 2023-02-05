from abc import ABC, abstractmethod

from src.models.notification import Notification


class Handler(ABC):
    """Абстрактный класс обработчика событий."""

    @abstractmethod
    async def get_data(self, msg: Notification):
        """Получить данные для события."""

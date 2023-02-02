"""Модуль с абстрактным брокером сообщений."""
from abc import ABC, abstractmethod


class Broker(ABC):
    """Абстрактный класс брокера."""

    @abstractmethod
    async def get_message(self) -> None:
        """Получить сообщение."""

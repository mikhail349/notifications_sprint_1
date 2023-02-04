"""Модуль абстрактных классов отправителя."""
from abc import ABC, abstractmethod


class Sender(ABC):
    """Абстрактный отправитель уведомления."""

    @abstractmethod
    async def send(self) -> None:
        """Отправить уведомление."""

"""Модуль абстрактных классов доставщика."""
from abc import ABC, abstractmethod


class Sender(ABC):
    """Абстрактный доставщик уведомления."""

    @abstractmethod
    async def send(self) -> None:
        """Отправить уведомление."""

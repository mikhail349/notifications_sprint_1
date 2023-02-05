"""Модуль абстрактных классов отправителя."""
from abc import ABC, abstractmethod
from typing import List


class Sender(ABC):
    """Абстрактный отправитель уведомления."""

    @abstractmethod
    async def send(self, text: str) -> None:  # recipients: List[str], 
        """Отправить уведомление."""

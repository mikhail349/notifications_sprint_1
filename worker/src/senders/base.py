"""Модуль абстрактных классов отправителя."""
from abc import ABC, abstractmethod
from typing import Optional

from src.storages.models.user import User


class Sender(ABC):
    """Абстрактный отправитель уведомления."""

    @abstractmethod
    async def send(
        self,
        recipient: User,
        text: str,
        subject: Optional[str] = None,
    ) -> None:
        """Отправить уведомление.

        Args:
            recipient: получатель `User`
            text: текст уведомления
            subject: тема уведомления

        """

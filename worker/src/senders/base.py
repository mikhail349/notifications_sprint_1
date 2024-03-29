"""Модуль абстрактных классов отправителя."""
from abc import ABC, abstractmethod

from src.storages.models.user import User


class Sender(ABC):
    """Абстрактный отправитель уведомления."""

    @abstractmethod
    async def send(
        self,
        recipient: User,
        text: str,
        **options,
    ) -> None:
        """Отправить уведомление.

        Args:
            recipient: получатель `User`
            text: текст уведомления
            options: доп. данные для уведомления

        """

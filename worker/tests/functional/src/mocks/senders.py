"""Модуль имитации отправки email."""
from typing import Optional

from src.senders.base import Sender
from src.storages.models.user import User


class MockedEmailSender(Sender):
    """Класс имитации отправки email."""

    def __init__(self) -> None:
        """Инициализировать класс имитации отправки email."""
        self.last_email: Optional[User] = None

    async def send(self, recipient: User, text: str, **options) -> None:
        self.last_recipient = recipient

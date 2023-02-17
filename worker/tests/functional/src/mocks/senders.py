"""Модуль имитации отправки email."""
from src.senders.base import Sender
from src.storages.models.user import User


class MockedEmailSender(Sender):
    """Класс имитации отправки email."""

    async def send(self, recipient: User, text: str, **options) -> None:
        self.last_email = {
            'recipient': recipient,
            'text': text,
            **options,
        }

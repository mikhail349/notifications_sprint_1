"""Модуль имитации отправки email."""
from typing import Dict, List

from src.senders.base import Sender
from src.storages.models.user import User


class MockedEmailSender(Sender):
    """
    Класс имитации отправки email.

    Хранит историю отправок `sendings`.
    """

    def __init__(self) -> None:
        """Инициализировать класс имитации отправки email."""
        self.sendings: List[Dict] = []

    def is_username_emailed(self, username: str) -> bool:
        """Проверить, была ли отправка по имени пользователя.

        Args:
            username: имя пользователя

        Returns:
            bool: Отправка была да или нет

        """
        for sending in self.sendings:
            recipient = sending.get('recipient')
            if recipient is not None and recipient.username == username:
                return True
        return False

    async def send(self, recipient: User, text: str, **options) -> None:
        self.sendings.append({
            'recipient': recipient,
            'text': text,
            **options,
        })

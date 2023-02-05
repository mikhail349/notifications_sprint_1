"""Модуль классов отправителя email."""
import logging
from typing import List

from src.senders import factory
from src.senders.base import Sender


class EmailSender(Sender):
    """Класс отправитель уведомлений по email."""

    async def send(self, text: str) -> None:  # recipients: List[str], 
        """Отправить уведомление."""
        msg = f"""
            subject: None
            text: {text}
        """
        logging.info(msg)


def initialize():
    """Зарегистрировать модуль в фабрике."""
    factory.register('src.senders.email', EmailSender)

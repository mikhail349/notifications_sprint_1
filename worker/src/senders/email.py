"""Модуль классов отправителя email."""
import logging

from src.senders import factory
from src.senders.base import Sender


class EmailSender(Sender):
    """Класс отправитель уведомлений по email."""

    async def send(self) -> None:
        """Отправить уведомление."""
        logging.info('Email отправлен.')


def initialize():
    """Зарегистрировать модуль в фабрике."""
    factory.register('src.senders.email', EmailSender)

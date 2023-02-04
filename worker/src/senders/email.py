"""Модуль классов доставщика email."""
from src.senders.base import Sender
from src.senders import factory

class EmailSender(Sender):
    """Класс доставщик уведомлений по email."""

    async def send(self) -> None:
        """Отправить уведомление."""
        import logging
        logging.info("Email отправлен.")


def initialize():
    """Зарегистрировать модуль в фабрике."""
    factory.register("src.senders.email", EmailSender)

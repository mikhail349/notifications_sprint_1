"""Модуль классов отправителя SMS."""
import logging
from typing import Optional

from src.senders import factory
from src.senders.base import Sender
from src.storages.models.user import User


class WebsocketSender(Sender):
    """Класс отправитель уведомлений по web socket."""

    async def send(
        self,
        recipient: User,
        text: str,
        subject: Optional[str] = None,
    ) -> None:
        msg = """
            Сообщение отправлено.
            username: {username}
            text: {text}
        """.format(
            username=recipient.username,
            text=text,
        )
        logging.info(msg)


def initialize():
    """Зарегистрировать модуль в фабрике."""
    factory.register('src.senders.websocket', WebsocketSender)

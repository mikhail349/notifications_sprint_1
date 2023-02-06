"""Модуль классов отправителя SMS."""
import logging
from typing import Optional

from src.senders.base import Sender
from src.storages.models.user import User


class SMSSender(Sender):
    """Класс отправитель уведомлений по sms."""

    async def send(
        self,
        recipient: User,
        text: str,
        subject: Optional[str] = None,
    ) -> None:
        if not recipient.notification_settings.allow_sms:
            return

        msg = """
            SMS отправлено.
            recipient: {phone_number}
            text: {text}
        """.format(
            phone_number=recipient.phone_number,
            text=text,
        )
        logging.info(msg)

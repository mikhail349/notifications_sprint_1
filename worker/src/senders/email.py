"""Модуль классов отправителя email."""
import logging
from typing import Optional

from src.senders import errors, messages
from src.senders.base import Sender
from src.storages.models.user import User


class EmailSender(Sender):
    """Класс отправитель уведомлений по email."""

    async def send(
        self,
        recipient: User,
        text: str,
        subject: Optional[str] = None,
    ) -> None:
        if not recipient.notification_settings.allow_email:
            raise errors.DeliveryNotAllowedError(
                messages.DELIVERY_NOT_ALLOWED,
            )

        msg = """
            Письмо отправлено.
            recipient: {email}
            subject: {subject}
            body: {text}
        """.format(
            email=recipient.email,
            subject=subject,
            text=text,
        )
        logging.info(msg)

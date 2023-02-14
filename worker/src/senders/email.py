"""Модуль классов отправителя email."""
import smtplib
from email.message import EmailMessage

from src.senders import errors, messages
from src.senders.base import Sender
from src.storages.models.user import User


class EmailSender(Sender):
    """Класс отправитель уведомлений по email.

    Args:
        host: хост
        port: порт
        username: имя пользователя
        password: пароль
        from_email: почта-адресант
    """

    def __init__(  # noqa: WPS211
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        from_email: str,
    ) -> None:
        """Инициализировать класс отправитель уведомлений по email.

        Args:
            host: хост
            port: порт
            username: имя пользователя
            password: пароль
            from_email: почта-адресант

        """
        self.from_email = from_email
        self.server = smtplib.SMTP_SSL(host, port)
        self.server.login(username, password)

    async def send(
        self,
        recipient: User,
        text: str,
        **options,
    ) -> None:
        if not recipient.notification_settings.allow_email:
            raise errors.DeliveryNotAllowedError(
                messages.DELIVERY_NOT_ALLOWED,
            )

        msg = EmailMessage()
        msg['FROM'] = self.from_email
        msg['TO'] = recipient.email
        msg['SUBJECT'] = options.get('subject', '')
        msg.add_alternative(text, subtype='html')

        self.server.sendmail(
            from_addr=self.from_email,
            to_addrs=[recipient.email],
            msg=msg.as_string(),
        )

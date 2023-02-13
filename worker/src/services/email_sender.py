"""Модуль инициализации отправителя по email."""
from src.config.smtp import smtp_config
from src.senders.base import Sender
from src.senders.email import EmailSender


def create_email_sender() -> Sender:
    """Создать отправителя по email.

    Returns:
        Sender: отправитель по email

    """
    return EmailSender(**smtp_config.dict())

"""Модуль фабрики отправителей."""
from typing import Callable, Dict

from src.senders.base import Sender

senders: Dict[str, Callable[..., Sender]] = {}


def register(sender_path: str, creation_fn: Callable[..., Sender]) -> None:
    """Зарегистрировать отправителя.

    Args:
        sender_path: путь отправителя
        creation_fn: функция инициализации отправителя

    """
    senders[sender_path] = creation_fn


def create(sender_path: str, *args, **kwargs) -> Sender:
    """Создать отправителя.

    Args:
        sender_path: путь отправителя
        args: доп. позиционные параметры
        kwargs: доп. именованные параметры

    Returns:
        Sender: отправитель

    """
    sender = senders[sender_path]
    return sender(*args, **kwargs)

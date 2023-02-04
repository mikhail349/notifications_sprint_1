"""Модуль фабрики доставщиков."""
from typing import Callable, Dict

from src.senders.base import Sender

senders: Dict[str, Callable[..., Sender]] = {}


def register(sender_path: str, creation_fn: Callable[..., Sender]) -> None:
    """Зарегистрировать доставщика.

    Args:
        sender_path: путь доставщика
        creation_fn: функция инициализации доставщика

    """
    senders[sender_path] = creation_fn

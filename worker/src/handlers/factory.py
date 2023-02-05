"""Модуль фабрики обработчиков."""
from typing import Callable, Dict

from src.handlers.base import Handler

handlers: Dict[str, Callable[..., Handler]] = {}


def register(sender_path: str, creation_fn: Callable[..., Handler]) -> None:
    """Зарегистрировать обработчика.

    Args:
        sender_path: путь обработчика
        creation_fn: функция инициализации обработчика

    """
    handlers[sender_path] = creation_fn


def create(handler_path: str, *args, **kwargs) -> Handler:
    """Создать обработчик.

    Args:
        handler_path: путь обработчика
        args: доп. позиционные параметры
        kwargs: доп. именованные параметры

    Returns:
        Handler: обработчик

    """
    handler = handlers[handler_path]
    return handler(*args, **kwargs)

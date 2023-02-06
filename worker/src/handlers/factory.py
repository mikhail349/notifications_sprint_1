"""Модуль фабрики обработчиков."""
from typing import Callable, Dict

from src.handlers.base import EventHandler

handlers: Dict[str, Callable[..., EventHandler]] = {}


def register(
    handler_path: str,
    creation_fn: Callable[..., EventHandler],
) -> None:
    """Зарегистрировать обработчика.

    Args:
        handler_path: путь обработчика
        creation_fn: функция инициализации обработчика

    """
    handlers[handler_path] = creation_fn


def create(handler_path: str, *args, **kwargs) -> EventHandler:
    """Создать обработчик.

    Args:
        handler_path: путь обработчика
        args: доп. позиционные параметры
        kwargs: доп. именованные параметры

    Returns:
        EventHandler: обработчик

    """
    event_handler = handlers[handler_path]
    return event_handler(*args, **kwargs)

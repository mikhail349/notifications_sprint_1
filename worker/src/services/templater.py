"""Модуль инициализации шаблонизатора."""
from src.templaters.base import Templater
from src.templaters.jinja import Jinja2Templater


def create_templater() -> Templater:
    """Создать шаблонизатор.

    Returns:
        Templater: шаблонизатор

    """
    return Jinja2Templater()

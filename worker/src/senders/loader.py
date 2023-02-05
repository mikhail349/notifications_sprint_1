"""Модуль загрущзи плагинов отправителей."""
import importlib
from abc import ABC, abstractmethod
from typing import List


class PluginModule(ABC):
    """Абстрактный класс модуля."""

    @staticmethod
    @abstractmethod
    def initialize():  # noqa: WPS605, WPS602
        """Инициализировать модуль."""


def load_module(name: str) -> PluginModule:
    """Загрузить модуль.

    Args:
        name: название модуля

    Returns:
        PluginModule: модуль
    """
    return importlib.import_module(name)


def load_plugins(plugins: List[str]) -> None:
    """Загрузить плагины.

    Args:
        plugins: список плагинов

    """
    for plugin in plugins:
        module = load_module(plugin)
        module.initialize()

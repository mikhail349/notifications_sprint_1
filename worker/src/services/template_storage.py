"""Модуль инициализации хранилища шаблонов."""
from src.storages.base import TemplateStorage
from src.storages.mock import MockedTemplateStorage


def create_template_storage() -> TemplateStorage:
    """Создать хранилище шаблонов.

    Returns:
        TemplateStorage: хранилище шаблонов

    """
    return MockedTemplateStorage()

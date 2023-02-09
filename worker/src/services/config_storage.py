"""Модуль инициализации хранилища шаблонов."""
from src.storages.base import ConfigStorage
from src.storages.mock import MockedConfigStorage


def create_config_storage() -> ConfigStorage:
    """Создать хранилище настроек.

    Returns:
        ConfigStorage: хранилище настроек

    """
    return MockedConfigStorage()

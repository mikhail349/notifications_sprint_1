"""Модуль инициализации хранилища данных."""
from src.storages.base import DataStorage
from src.storages.mock import MockedDataStorage


def create_data_storage() -> DataStorage:
    """Создать хранилище данных.

    Returns:
        DataStorage: хранилище данных

    """
    return MockedDataStorage()

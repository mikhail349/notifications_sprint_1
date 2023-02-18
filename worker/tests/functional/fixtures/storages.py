"""Модуль с фикстурами хранилищ."""
import pytest

from tests.functional.src.mocks import storages


@pytest.fixture
def notification_storage() -> storages.MockedNotificationStorage:
    """Фикстура хранилища уведомлений.

    Returns:
        MockedNotificationStorage: класс хранилища уведомлений.

    """
    return storages.MockedNotificationStorage()


@pytest.fixture
def data_storage() -> storages.MockedDataStorage:
    """Фикстура хранилища данных.

    Returns:
        MockedDataStorage: класс хранилища данных.

    """
    return storages.MockedDataStorage()


@pytest.fixture
def config_storage() -> storages.MockedConfigStorage:
    """Фикстура хранилища настроек.

    Returns:
        MockedConfigStorage: класс хранилища настроек.

    """
    return storages.MockedConfigStorage()

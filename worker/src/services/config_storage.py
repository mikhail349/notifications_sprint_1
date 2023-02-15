"""Модуль инициализации хранилища шаблонов."""
from src.config.admin_panel import admin_panel_config
from src.storages.base import ConfigStorage
from src.storages.configuration import AdminPanelConfigurationStorage


def create_config_storage() -> ConfigStorage:
    """Создать хранилище настроек.

    Returns:
        ConfigStorage: хранилище настроек

    """
    return AdminPanelConfigurationStorage(**admin_panel_config.dict())

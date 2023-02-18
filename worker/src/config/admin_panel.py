"""Настройки для работы с сервисом admin panel."""
from pydantic import Field

from src.config.base import BaseConfig


class AdminPanelSettings(BaseConfig):
    """Настройки Admin panel."""

    api_url: str = Field('127.0.0.1:8080/api/v1', env='ADMIN_PANEL_API')


admin_panel_config = AdminPanelSettings()

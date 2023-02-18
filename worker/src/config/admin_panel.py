"""Настройки для работы с сервисом admin panel."""
from pydantic import Field, Required

from src.config.base import BaseConfig


class AdminPanelSettings(BaseConfig):
    """Настройки Admin panel."""

    api_url: str = Field(Required, env='ADMIN_PANEL_API')


admin_panel_config = AdminPanelSettings()

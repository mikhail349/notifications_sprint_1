"""Настройки проекта."""
from pydantic import Field

from src.config.base import BaseConfig


class ProjectSettings(BaseConfig):
    """Настройки проекта."""

    title: str = Field('API сервиса уведомлений.', env='PROJECT_TITLE')
    """Название проекта."""
    description: str = Field(
        'Позволяет отправлять уведомления клиентам.',
        env='PROJECT_DESC',
    )
    """Описание проекта."""
    version: str = Field('1.0.0', env='PROJECT_VER')
    """Версия проекта."""


project_settings = ProjectSettings()

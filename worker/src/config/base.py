"""Модуль базовых настроек сервиса."""
from pathlib import Path

from pydantic import BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent.parent.parent
"""Корень проекта."""

DEFAULT_EMAIL_CONFIRMATION_EXPIRES = 60
"""
Кол-во секунд по умолчанию,
сколько действительна ссылка подтверждения email.
"""


class BaseConfig(BaseSettings):
    """Базовый класс для конфигураций, получающих значений из .env файла."""

    email_confirmation_expires: int = Field(
        default=DEFAULT_EMAIL_CONFIRMATION_EXPIRES,
        env='EMAIL_CONFIRMATION_EXPIRES',
    )
    """Кол-во секунд, сколько действительна ссылка подтверждения email."""

    class Config(BaseSettings.Config):
        """Базовый мета-класс для переопреления доп. параметров."""

        env_file = BASE_DIR.joinpath('.env')

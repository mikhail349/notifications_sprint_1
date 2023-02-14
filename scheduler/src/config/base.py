"""Модуль базовых настроек сервиса."""
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
"""Корень проекта."""


class BaseConfig(BaseSettings):
    """Базовый класс для конфигураций, получающих значений из .env файла."""

    class Config(BaseSettings.Config):
        """Базовый мета-класс для переопреления доп. параметров."""

        env_file = BASE_DIR.joinpath('.env')

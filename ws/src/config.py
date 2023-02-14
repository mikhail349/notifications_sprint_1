"""Модуль настроек приложения."""
import os

from pydantic import BaseSettings as PydanticBaseSettings
from pydantic import Field, Required

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)),
)
"""Корень проекта."""


class BaseSettings(PydanticBaseSettings):
    """Базовый класс для конфигураций, получающих значений из .env файла."""

    class Config(PydanticBaseSettings.Config):
        """Базовый мета-класс для переопреления доп. параметров."""

        env_file = os.path.join(BASE_DIR, '.env')


class JWTSettings(BaseSettings):
    """Настройки JWT."""

    algorithm: str = Field('RS256', env='JWT_ALGORITHM')
    """Алгоритм шифрования."""
    public_key_path: str = Field(Required, env='JWT_PUBLIC_KEY_PATH')
    """Путь до публичного RSA ключа."""


jwt_settings = JWTSettings()

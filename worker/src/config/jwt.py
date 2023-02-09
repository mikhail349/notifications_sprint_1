"""Модуль настроек JWT."""
from pydantic import Field

from src.config.base import BaseConfig

DEFAULT_EXPIRES = 60
"""Кол-во секунд по умолчанию, сколько действителен токен."""


class JWTConfig(BaseConfig):
    """Класс настроек JWT."""

    secret: str = Field('topsecretvalue', env='JWT_SECRET')
    """Секретный ключ."""
    algorithm: str = Field('HS256', env='JWT_ALGORITHM')
    """Алгоритм шифрования."""
    expires: int = Field(DEFAULT_EXPIRES, env='JWT_EXPIRES')
    """Кол-во секунд, сколько действителен токен."""


jwt_config = JWTConfig()

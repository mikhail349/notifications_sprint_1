"""Модуль настроек MongoDB."""
from pydantic import Field, Required

from src.config.base import BaseConfig

DEFAULT_PORT = 27017
"""Порт по умолчанию."""


class MongoConfig(BaseConfig):
    """Настройки MongoDB."""

    host: str = Field('127.0.0.1', env='MONGO_HOST')
    """Имя хоста."""
    port: int = Field(DEFAULT_PORT, env='MONGO_PORT')
    """Номер порта."""
    db: str = Field('notifications', env='MONGO_DB')
    """Название БД."""
    username: str = Field(Required, env='MONGO_USER')
    """Имя пользователя."""
    password: str = Field(Required, env='MONGO_PASS')
    """Пароль."""


mongo_config = MongoConfig()

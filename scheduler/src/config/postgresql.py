"""Настройки PostgreSQL."""
from pydantic import Field, Required
from src.config.base import BaseConfig


class PSQLSettings(BaseConfig):
    """Настройки PostgreSQL."""

    user: str = Field(Required, env='POSTGRES_USER')
    """Имя пользователя."""
    password: str = Field(Required, env='POSTGRES_PASSWORD')
    """Пароль."""
    host: str = Field(Required, env='POSTGRES_HOST')
    """Хост."""
    port: int = Field(5432, env='POSTGRES_PORT')
    """Порт."""
    dbname: str = Field('postgres', env='POSTGRES_DB')

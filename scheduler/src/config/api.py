"""Настройки API сервиса нотификаций."""
from pydantic import Field, Required
from src.config.base import BaseConfig


class APISettings(BaseConfig):
    """Настройки API сервиса нотификаций."""

    host: str = Field(Required, env='API_HOST')
    """Хост."""
    port: str = Field(Required, env='API_PORT')
    """Порт."""

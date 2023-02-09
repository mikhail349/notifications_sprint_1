"""Настройки Bitly."""
from pydantic import Field, Required

from src.config.base import BaseConfig


class BitlySettings(BaseConfig):
    """Настройки Bitly."""

    api_url: str = Field('https://api-ssl.bitly.com/v4/shorten', env='BITLY_API_URL')
    """URL для укорачивания ссылки."""
    token: str = Field(Required, env='BITLY_TOKEN')
    """Токен доступа API."""

bitly_settings = BitlySettings()

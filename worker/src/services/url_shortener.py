"""Модуль инициализации укорачивателя ссылок."""
from src.config.bitly import bitly_settings
from src.url_shorteners.base import URLShortener
from src.url_shorteners.bitly import BitlyURLShortener


def create_url_shortener() -> URLShortener:
    """Создать укорачивателя ссылок.

    Returns:
        URLShortener: укорачиватель ссылок

    """
    return BitlyURLShortener(**bitly_settings.dict())

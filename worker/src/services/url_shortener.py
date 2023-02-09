"""Модуль инициализации укорачивателя ссылок."""
from src.url_shorteners.base import URLShortener
from src.url_shorteners.mock import MockedURLShortener


def create_url_shortener() -> URLShortener:
    """Создать укорачивателя ссылок.

    Returns:
        URLShortener: укорачиватель ссылок

    """
    return MockedURLShortener()

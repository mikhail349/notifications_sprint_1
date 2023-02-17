"""Модуль имитации укорачивателя ссылок."""
from src.url_shorteners.base import URLShortener


class MockedURLShortener(URLShortener):
    """Класс имитации укорачивателя ссылок."""

    async def shorten(self, url: str) -> str:
        return 'https://sh/dsk2k'

"""Модуль с базовым укорачивателем ссылок."""
from abc import ABC, abstractmethod


class URLShortener(ABC):
    """Абстрактный класс укорачивателя ссылок."""

    @abstractmethod
    async def shorten(self, url: str) -> str:
        """Укоротить ссылку.

        Args:
            url: длинная ссылка

        Returns:
            str: короткая ссылка

        """


class URLShortenerMixin(object):
    """Миксин, добавляющий url_shortener в класс."""

    def __init__(self, url_shortener: URLShortener, *args, **kwargs):
        """Инициализировать миксин, добавляющий url_shortener в класс.

        Args:
            url_shortener: укорачиватель ссылок
            args: позиционные аргументы основного класса
            kwargs: именные аргументы основного класса

        """
        super().__init__(*args, **kwargs)
        self.url_shortener = url_shortener

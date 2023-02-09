"""Модуль укорачивателя ссылок Bitly."""
import aiohttp
from http import HTTPStatus

from src.url_shorteners.base import URLShortener
from src.url_shorteners.errors import URLShortenBaseError


class BitlyURLShortener(URLShortener):
    """Класс укорачивателя ссылок Bitly.

    Args:
        api_url: URL для укорачивания ссылки
        token: токен доступа к API

    """

    def __init__(self, api_url: str, token: str) -> None:
        """Инициализировать класс укорачивателя ссылок Bitly.

        Args:
            api_url: URL для укорачивания ссылки
            token: токен доступа к API

        """
        self.api_url = api_url
        self.token = token

    async def shorten(self, url: str) -> str:
        headers = {
            'Authorization': "Bearer {token}".format(token=self.token)
        }
        post_data = {
            'long_url': url
        }
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(self.api_url, json=post_data) as response:
                response_json = await response.json()
                response_status = response.status
                if not response_status == HTTPStatus.CREATED:
                    raise URLShortenBaseError(response_json['message'])
                return response_json['link']

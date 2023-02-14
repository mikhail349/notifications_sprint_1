"""Модуль классов отправителя по web socket."""
import json

import websockets

from src.senders.base import Sender
from src.storages.models.user import User


class WebsocketSender(Sender):
    """Класс отправитель уведомлений по web socket.

    Args:
        host: хост
        port: порт
        token: access-токен для подключения
        api_url: URL для отправки сообщений

    """

    def __init__(self, host: str, port: int, token: str, api_url: str):
        """Инициализировать класс отправитель уведомлений по web socket.

        Args:
            host: хост
            port: порт
            token: access-токен для подключения
            api_url: URL для отправки сообщений

        """
        self.host = host
        self.port = port
        self.token = token
        self.api_url = api_url

    async def send(
        self,
        recipient: User,
        text: str,
        **options,
    ) -> None:
        url = 'ws://{host}:{port}/{api}?token={token}'.format(
            host=self.host,
            port=self.port,
            api=self.api_url,
            token=self.token,
        )
        msg = {
            'username': recipient.username,
            'text': text,
        }
        async with websockets.connect(url) as websocket:
            await websocket.send(json.dumps(msg))

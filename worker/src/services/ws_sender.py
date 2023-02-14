"""Модуль инициализации отправителя по WebSocket."""
from src.config.ws import ws_config
from src.senders.base import Sender
from src.senders.websocket import WebsocketSender
from src.storages.base import DataStorage


async def create_ws_sender(data_storage: DataStorage) -> Sender:
    """Создать отправителя по WebSocket.

    Args:
        data_storage: хранилище данных

    Returns:
        Sender: отправитель по WebSocket

    """
    access_token, _ = await data_storage.login(
        username=ws_config.username,
        password=ws_config.password,
    )
    return WebsocketSender(
        host=ws_config.host,
        port=ws_config.port,
        token=access_token,
        api_url=ws_config.api_url,
    )

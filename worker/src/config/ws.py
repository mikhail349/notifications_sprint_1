"""Модуль настроек WebSocket."""
from pydantic import Field, Required

from src.config.base import BaseConfig

DEFAULT_PORT = 8081
"""Порт по умолчанию."""


class WSConfig(BaseConfig):
    """Настройки WebSocket."""

    host: str = Field('127.0.0.1', env='WS_HOST')
    """Имя хоста."""
    port: int = Field(DEFAULT_PORT, env='WS_PORT')
    """Номер порта."""
    username: str = Field(Required, env='WS_USERNAME')
    """Имя пользователя."""
    password: str = Field(Required, env='WS_PASSWORD')
    """Пароль."""
    api_url: str = Field('api/v1/send_messages', env='WS_API_URL')
    """Эндпоинт для передачи сообщений."""


ws_config = WSConfig()

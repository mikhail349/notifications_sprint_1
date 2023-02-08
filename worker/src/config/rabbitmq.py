"""Настройки RabbitMQ."""
from pydantic import Field, Required

from src.config.base import BaseConfig

DEFAULT_PORT = 5672
"""Порт подключения по умолчанию."""
DEFAULT_CONSUMPTION_DELAY = 1
"""Задержка при чтении очереди по умолчанию, секунд."""


class RabbitMQSettings(BaseConfig):
    """Настройки RabbitMQ."""

    username: str = Field(Required, env='RABBITMQ_USER')
    """Имя пользователя."""
    password: str = Field(Required, env='RABBITMQ_PASS')
    """Пароль."""
    host: str = Field('127.0.0.1', env='RABBITMQ_HOST')
    """Хост."""
    port: int = Field(DEFAULT_PORT, env='RABBITMQ_PORT')
    """Порт."""
    consumption_delay: int = Field(
        default=DEFAULT_CONSUMPTION_DELAY,
        env='RABBITMQ_CONSUMPTION_DELAY'
    )
    """Задержка при чтении очереди, секунд."""


rabbitmq_settings = RabbitMQSettings()

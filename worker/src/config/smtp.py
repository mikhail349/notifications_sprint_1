"""Модуль настроек SMTP."""
from pydantic import Field, Required

from src.config.base import BaseConfig

DEFAULT_PORT = 465
"""Порт по умолчанию."""


class SMTPConfig(BaseConfig):
    """Настройки SMTP."""

    host: str = Field('127.0.0.1', env='SMTP_HOST')
    """Имя хоста."""
    port: int = Field(DEFAULT_PORT, env='SMTP_PORT')
    """Номер порта."""
    username: str = Field(Required, env='SMTP_USERNAME')
    """Имя пользователя."""
    password: str = Field(Required, env='SMTP_PASSWORD')
    """Пароль."""
    from_email: str = Field(Required, env='SMTP_FROM_EMAIL')
    """Почта-адресант."""


smtp_config = SMTPConfig()

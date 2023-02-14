"""Модуль сообщений."""
from pydantic import BaseModel


class Message(BaseModel):
    """Модель сообщения."""

    username: str
    text: str

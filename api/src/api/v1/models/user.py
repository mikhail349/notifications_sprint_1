"""Модуль моделей событий пользователя."""
import datetime

from pydantic import BaseModel


class User(BaseModel):
    """Модель пользователя."""

    username: str
    created_at: datetime.datetime

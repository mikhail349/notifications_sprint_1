"""Модуль моделей событий пользователя."""
import datetime

from pydantic import BaseModel

from src.api.v1.models.base import Event


class User(BaseModel):
    """Модель пользователя."""

    username: str
    created_at: datetime.datetime


class UserEvent(Event):
    """Модель события пользователя."""

    body: User

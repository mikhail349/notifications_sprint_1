"""Модуль с моделями."""
from pydantic import BaseModel


class User(BaseModel):
    """Модель пользователя."""

    username: str
    is_superuser: bool
    permissions: list[str]

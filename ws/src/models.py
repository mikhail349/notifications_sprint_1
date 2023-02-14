"""Модуль с моделями."""
from typing import List

from pydantic import BaseModel


class User(BaseModel):
    """Модель пользователя."""

    username: str
    is_superuser: bool
    permissions: List[str]

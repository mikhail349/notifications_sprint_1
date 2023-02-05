"""Модели пользователя."""
from pydantic import BaseModel


class User(BaseModel):
    """Модель пользователя."""

    username: str
    name: str
    email: str
    phone_number: str

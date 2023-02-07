"""Модели пользователя."""
from pydantic import BaseModel


class UserNotificationSettings(BaseModel):
    """Модель настроек уведомлений пользователя."""

    allow_email: bool


class User(BaseModel):
    """Модель пользователя."""

    username: str
    name: str
    email: str
    phone_number: str
    notification_settings: UserNotificationSettings

"""Модуль моделей событий пользователя."""
import datetime
import uuid

from pydantic import BaseModel


class Mass(BaseModel):
    """Модель массовой рассылки."""

    cohort: str
    template_id: uuid.UUID
    subject: str

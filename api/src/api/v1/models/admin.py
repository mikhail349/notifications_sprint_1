"""Модуль моделей событий пользователя."""
import uuid

from pydantic import BaseModel

from src.api.v1.models.base import Event
from src.models.base import DeliveryType


class AdminModel(BaseModel):
    """Модель админ панели."""

    cohort: str
    template_id: uuid.UUID
    subject: str


class AdminEvent(Event):
    """Модель события из админ панели."""

    body: AdminModel
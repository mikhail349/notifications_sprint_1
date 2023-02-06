"""Модуль моделей событий пользователя."""
import uuid

from pydantic import BaseModel

from src.models.base import DeliveryType


class AdminEvent(BaseModel):
    """Модель события из админ панели."""

    cohort: str
    template_id: uuid.UUID
    subject: str
    deliver_type: DeliveryType

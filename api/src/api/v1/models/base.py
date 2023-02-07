"""Модуль базовой модели."""
from pydantic import BaseModel

from src.models.base import DeliveryType, PriorityType


class Event(BaseModel):
    """Модель базового события."""

    delivery_type: DeliveryType
    priority: PriorityType

"""Модуль базовой модели."""
import enum

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    """Базовая модель."""

class DeliveryType(str, enum.Enum):
    """Перечисление способов доставки."""
    EMAIL = 'email'
    SMS = 'sms'

class EventType(str, enum.Enum):
    """Перечисление типов событий."""
    REVIEW_RATED = 'review-reporting.v1.rated'  # noqa: WPS115

class Event(BaseModel):
    """Модель базового события."""
    delivery_type: DeliveryType

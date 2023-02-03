"""Модуль базовой модели."""
import enum

from pydantic import BaseModel


class DeliveryType(enum.Enum):
    """Перечисление способов доставки."""

    EMAIL = 'email'  # noqa: WPS115
    SMS = 'sms'  # noqa: WPS115


class Event(BaseModel):
    """Модель базового события."""

    delivery_type: DeliveryType

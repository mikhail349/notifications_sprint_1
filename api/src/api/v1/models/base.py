"""Модуль базовой модели."""
import enum

from pydantic import BaseModel


class DeliveryType(str, enum.Enum):
    """Перечисление способов доставки."""
    EMAIL = 'email'
    SMS = 'sms'

class Event(BaseModel):
    """Модель базового события."""
    delivery_type: DeliveryType

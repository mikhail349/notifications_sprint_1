"""Модуль базовой модели."""
import enum

from pydantic import BaseModel


class DeliveryType(str, enum.Enum):  # noqa: WPS600
    """Перечисление способов доставки."""

    EMAIL = 'email'
    SMS = 'sms'
    WEB_SOCKET = "websocket"


class Event(BaseModel):
    """Модель базового события."""

    delivery_type: DeliveryType

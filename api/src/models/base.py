"""Модуль базовых моделей."""
import enum

from pydantic import BaseModel


class DeliveryType(enum.Enum):
    """Перечисление способов доставки."""

    EMAIL = 'email'
    SMS = 'sms'
    WEB_SOCKET = "websocket"


class EventType(enum.Enum):
    """Перечисление типов событий."""

    REVIEW_RATED = 'review-reporting.v1.rated'
    USER_REGISTERED = 'user-reporting.v1.registered'
    ADMIN = 'admin-reporting.v1.event'


class Notification(BaseModel):
    """Модель базового уведомления."""

    delivery_type: DeliveryType
    event_type: EventType
    body: BaseModel

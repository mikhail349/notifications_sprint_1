"""Модуль базовых моделей сервиса."""
import enum

from pydantic import BaseModel


class DeliveryType(str, enum.Enum):  # noqa: WPS600
    """Перечисление способов доставки."""

    EMAIL = 'email'
    SMS = 'sms'
    WEB_SOCKET = 'websocket'


class EventType(str, enum.Enum):  # noqa: WPS600
    """Перечисление типов событий."""

    REVIEW_RATED = 'review-reporting.v1.rated'
    USER_REGISTERED = 'user-reporting.v1.registered'
    ADMIN = 'admin-reporting.v1.event'


class Message(BaseModel):
    """Модель базового сообщения."""

    delivery_type: DeliveryType
    event_type: EventType
    body: dict

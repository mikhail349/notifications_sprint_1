"""Модуль базовых моделей."""
import enum

from pydantic import BaseModel


class DeliveryType(str, enum.Enum):  # noqa: WPS600
    """Перечисление способов доставки."""

    EMAIL = 'email'
    WEB_SOCKET = 'websocket'


class EventType(enum.Enum):
    """Перечисление типов событий."""

    REVIEW_RATED = 'review-reporting.v1.rated'
    USER_REGISTERED = 'user-reporting.v1.registered'
    ADMIN = 'admin-reporting.v1.event'


class PriorityType(enum.Enum):
    """Перечисление приоритетов."""

    LOW = 'low'
    HIGH = 'high'


class Message(BaseModel):
    """Модель базового сообщения."""

    delivery_type: DeliveryType
    event_type: EventType
    body: BaseModel

"""Модуль базовых моделей."""
import enum

from pydantic import BaseModel


class DeliveryType(enum.Enum):
    """Перечисление способов доставки."""

    EMAIL = 'email'  # noqa: WPS115
    SMS = 'sms'  # noqa: WPS115


class EventType(enum.Enum):
    """Перечисление типов событий."""

    REVIEW_RATED = 'review-reporting.v1.rated'  # noqa: WPS115
    USER_REGISTERED = 'user-reporting.v1.registered'  # noqa: WPS115


class Notification(BaseModel):
    """Модель базового уведомления."""

    delivery_type: DeliveryType
    event_type: EventType
    body: BaseModel

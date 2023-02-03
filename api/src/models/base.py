import enum

from pydantic import BaseModel


class DeliveryType(enum.Enum):
    """Перечисление способов доставки."""
    EMAIL = 'email'
    SMS = 'sms'


class EventType(str, enum.Enum):
    """Перечисление типов событий."""
    REVIEW_RATED = 'review-reporting.v1.rated'  # noqa: WPS115


class QueueType(enum.Enum):
    """Перечисление типов очередей."""
    LOW_PRIORITY = 'low_priority'  # noqa: WPS115
    HIGH_PRIORITY = 'high_priority'  # noqa: WPS115


class Notification(BaseModel):
    """Модель базового уведомления."""
    delivery_type: DeliveryType
    event_type: EventType
    body: BaseModel

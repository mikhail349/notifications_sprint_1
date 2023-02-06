"""Модуль уведомлений."""
import datetime
import enum
from typing import Optional

from pydantic import BaseModel

from src.models.message import DeliveryType, EventType


class Status(enum.Enum):
    """Статус уведомления."""

    SUCCESS = 'success'
    ERROR = 'error'


class Notification(BaseModel):
    """Модель уведомлений."""

    delivery_type: DeliveryType
    event_type: EventType
    body: dict
    attempted_at: datetime.datetime
    status: Status
    comments: Optional[str] = None

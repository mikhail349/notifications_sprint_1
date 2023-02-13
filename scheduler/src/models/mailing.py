"""Модель рассылок."""
import enum
import uuid
from datetime import datetime

from pydantic import BaseModel


class Periodicity(enum.Enum):
    """Значения периодичности рассылок."""

    once = 'once'
    daily = 'daily'
    weekly = 'weekly'
    monthly = 'monthly'


class Channel(enum.Enum):
    """Значения способов рассылок."""

    email = 'email'
    websocket = 'websocket'


class Priority(enum.Enum):
    """Значения приоритетов рассылок."""

    low = 'low'
    high = 'high'


class AdminEvent(BaseModel):
    """Модель рассылки, настроенной в панели администратора."""

    id: uuid.UUID
    user_group: str
    template_id: uuid.UUID
    subject: str
    channel: Channel
    periodicity: Periodicity
    priority: Priority
    next_planned_date: datetime

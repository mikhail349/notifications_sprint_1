"""Модуль моделей обработчика."""
from pydantic import BaseModel

from src.models.notification import EventType


class EventHandler(BaseModel):
    """Модель сопоставления типа события и обработчика."""

    event_type: EventType
    handler_plugin: str

"""Модуль моделей отправителя."""
from pydantic import BaseModel

from src.models.notification import DeliveryType


class DeliverySender(BaseModel):
    """Модель сопоставления типа доставки и отправителя."""

    delivery_type: DeliveryType
    sender_plugin: str

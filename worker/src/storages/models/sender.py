from pydantic import BaseModel

from src.models.notification import DeliveryType


class DeliverySender(BaseModel):
    delivery_type: DeliveryType
    sender_plugin: str

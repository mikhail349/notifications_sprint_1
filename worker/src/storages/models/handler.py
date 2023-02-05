from pydantic import BaseModel

from src.models.notification import EventType


class EventHandler(BaseModel):
    event_type: EventType
    handler_plugin: str

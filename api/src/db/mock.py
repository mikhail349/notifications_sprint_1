from src.db.base import DataBase

from src.models.base import EventType, PriorityType


class MockDataBase(DataBase):
    """Класс имитации базы данных."""

    async def get_priority(self, event_type: EventType) -> PriorityType:
        mapping = {
            EventType.REVIEW_RATED: PriorityType.HIGH_PRIORITY
        }
        return mapping.get(event_type, PriorityType.LOW_PRIORITY)

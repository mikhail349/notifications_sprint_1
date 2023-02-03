from abc import ABC, abstractmethod

from src.models.base import EventType, PriorityType


class DataBase(ABC):
    """Абстрактный класс базы данных."""

    @abstractmethod
    async def get_priority(self, event_type: EventType) -> PriorityType:
        """Получить приоритет по типу события.

        Args:
            event_type: тип события

        Returns:
            `PriorityType`: приоритет

        """
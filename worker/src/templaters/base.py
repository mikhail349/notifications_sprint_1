"""Модуль абстрактного шаблонизатора."""
from abc import ABC, abstractmethod
from typing import Dict

from src.models.notification import DeliveryType, EventType


class Templater(ABC):
    """Абстраткный класс шаблонизатора."""

    @abstractmethod
    async def get_template(
        self,
        delivery_type: DeliveryType,
        event_type: EventType,
    ) -> str:
        """Получить шаблон уведомления.

        Args:
            delivery_type: способ доставки
            event_type: тип события

        Returns
            str: шаблон

        """

    @abstractmethod
    def get_filled_template(self, template: str, data: Dict) -> str:
        """Заполнить шаблон данными.

        Args:
            template: шаблон
            data: данные
        
        Returns:
            str: заполненный шаблон

        """

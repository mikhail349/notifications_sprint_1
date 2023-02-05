"""Модуль абстрактного шаблонизатора."""
from abc import ABC, abstractmethod
from typing import Dict


class Templater(ABC):
    """Абстраткный класс шаблонизатора."""

    @abstractmethod
    def get_filled_template(self, template: str, data: Dict) -> str:
        """Заполнить шаблон данными.

        Args:
            template: шаблон
            data: данные
        
        Returns:
            str: заполненный шаблон

        """

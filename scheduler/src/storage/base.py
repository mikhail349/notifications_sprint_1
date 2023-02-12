"""Модуль с абстрактным классом хранилища."""
from abc import ABC, abstractmethod


class Storage(ABC):
    """Абстрактное хранилище."""

    @abstractmethod
    def get_pending_notifications(self):
        """Получить список рассылок с датой меньше или равной текуущей."""

    @abstractmethod
    def update_processed_notifications(self):
        """Обновить запланированную дату рассылки после отправки в очередь."""

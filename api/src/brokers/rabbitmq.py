"""Модуль RabbitMQ."""
import enum

import aio_pika

from src.brokers.base import Broker
from src.models.base import Notification, EventType


class RoutingKey(str, enum.Enum):
    """Перечисление ключей маршрутизации."""

    LOW_PRIORITY = 'low_priority'  # noqa: WPS115
    HIGH_PRIORITY = 'high_priority'  # noqa: WPS115


def get_routing_key(event_type: EventType) -> RoutingKey:
    """Получить ключ маршрутизации по типу события.
    
    Args:
        event_type: тип события

    Returns:
        `RoutingKey`: ключ маршрутизации

    """
    mapping = {
        EventType.REVIEW_RATED: RoutingKey.HIGH_PRIORITY
    }
    return mapping.get(event_type, RoutingKey.LOW_PRIORITY)


class RabbitMQ(Broker):
    """Класс RabbitMQ.

    Args:
        exchange: точка обмена `AbstractExchange`

    """

    def __init__(self, exchange: aio_pika.abc.AbstractExchange) -> None:
        """Инициализировать класс RabbitMQ.

        Args:
            exchange: точка обмена `AbstractExchange`

        """
        self.exchange = exchange

    async def _post(self, routing_key: RoutingKey, payload: Notification) -> None:
        """Вспомогательный метод отправки уведомления.

        Args:
            routing_key: перечисление `RoutingKey`
            payload: инстанс класса `Event`

        """
        message = aio_pika.Message(
            body=payload.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(
            message=message,
            routing_key=routing_key.value,
        )
    
    async def post(self, notification: Notification) -> None:
        """Отправить уведомление в очередь.

        Args:
            notification: инстанс уведомления `Notification`

        """
        routing_key = get_routing_key(notification.event_type)
        await self._post(routing_key=routing_key, payload=notification)

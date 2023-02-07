"""Модуль API-запросов событий."""
from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from src.api.v1.models.admin import AdminEvent
from src.brokers.base import Broker
from src.models.base import EventType, Message
from src.services import broker

router = APIRouter(prefix='/admin', tags=['Админ-панель'])


@router.post(
    path='/',
    summary='Событие из админ-панели',
)
async def post_admin_event(
    admin_event: AdminEvent,
    broker: Broker = Depends(broker.get_broker),  # noqa: WPS404, B008
) -> Response:
    """Отправить событие массовой рассылки.

    Args:
        admin_event: модель события `AdminEvent`
        broker: брокер сообщений

    Returns:
        Response: http ответ

    """
    message = Message(
        delivery_type=admin_event.delivery_type,
        event_type=EventType.ADMIN,
        body=admin_event.body,
    )
    await broker.post(priority=admin_event.priority, message=message)
    return Response(status_code=HTTPStatus.OK)

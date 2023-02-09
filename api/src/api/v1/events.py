"""Модуль API-запросов событий."""
from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from src.api.v1.models.review import ReviewRatingEvent
from src.api.v1.models.user import UserEvent
from src.brokers.base import Broker
from src.models.base import EventType, Message
from src.services import broker

router = APIRouter(prefix='/events', tags=['События'])


@router.post('/review_rating', summary='Событие оценки рецензии')
async def post_review_rating(
    review_rating_event: ReviewRatingEvent,
    broker: Broker = Depends(broker.get_broker),  # noqa: WPS404, B008
) -> Response:
    """Отправить событие оценки рецензии.

    Args:
        review_rating_event: модель события оценки рецензии `ReviewRatingEvent`
        broker: брокер сообщений

    Returns:
        Response: http ответ

    """
    message = Message(
        delivery_type=review_rating_event.delivery_type,
        event_type=EventType.REVIEW_RATED,
        body=review_rating_event.body,
    )
    await broker.post(
        priority=review_rating_event.priority,
        message=message,
    )
    return Response(status_code=HTTPStatus.OK)


@router.post(
    path='/user_registered',
    summary='Событие регистрации нового пользователя',
)
async def post_user_registered(
    user_event: UserEvent,
    broker: Broker = Depends(broker.get_broker),  # noqa: WPS404, B008
) -> Response:
    """Отправить событие регистрации нового пользователя.

    Args:
        user_event: модель события пользователя `UserEvent`
        broker: брокер сообщений

    Returns:
        Response: http ответ

    """
    message = Message(
        delivery_type=user_event.delivery_type,
        event_type=EventType.USER_REGISTERED,
        body=user_event.body,
    )
    await broker.post(priority=user_event.priority, message=message)
    return Response(status_code=HTTPStatus.OK)

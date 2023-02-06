"""Модуль API-запросов событий."""
from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from src.api.v1.models.mass import Mass
from src.api.v1.models.review import ReviewRatingEvent
from src.api.v1.models.user import User
from src.brokers.base import Broker
from src.models.base import DeliveryType, EventType, Notification
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
    notification = Notification(
        delivery_type=review_rating_event.delivery_type,
        event_type=EventType.REVIEW_RATED,
        body=review_rating_event.body,
    )
    await broker.post(notification)
    return Response(status_code=HTTPStatus.OK)


@router.post(
    path='/user_registered',
    summary='Событие регистрации нового пользователя',
)
async def post_user_registered(
    user: User,
    broker: Broker = Depends(broker.get_broker),  # noqa: WPS404, B008
) -> Response:
    """Отправить событие регистрации нового пользователя.

    Args:
        user: модель пользователя `User`
        broker: брокер сообщений

    Returns:
        Response: http ответ

    """
    notification = Notification(
        delivery_type=DeliveryType.EMAIL,
        event_type=EventType.USER_REGISTERED,
        body=user,
    )
    await broker.post(notification)
    return Response(status_code=HTTPStatus.OK)


@router.post(
    path='/mass',
    summary='Событие массовой рассылки',
)
async def post_mass(
    mass: Mass,
    broker: Broker = Depends(broker.get_broker),  # noqa: WPS404, B008
) -> Response:
    """Отправить событие массовой рассылки.

    Args:
        mass: модель массовой рассылки `Mass`
        broker: брокер сообщений

    Returns:
        Response: http ответ

    """
    notification = Notification(
        delivery_type=DeliveryType.EMAIL,
        event_type=EventType.MASS,
        body=mass,
    )
    await broker.post(notification)
    return Response(status_code=HTTPStatus.OK)

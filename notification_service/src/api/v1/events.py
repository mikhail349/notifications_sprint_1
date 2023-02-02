"""Модуль API-запросов событий."""
from http import HTTPStatus

from fastapi import APIRouter, Response, Depends

from src.models.review import ReviewRating
from src.services import broker
from src.brokers.base import Broker

router = APIRouter(prefix='/events', tags=['События'])


@router.post('/review_rating', summary='Событие оценки рецензии')
async def post_review_rating(
    review_rating: ReviewRating,
    broker: Broker = Depends(broker.get_broker)
) -> Response:
    """Отправить событие оценки рецензии.

    Args:
        review_rating: модель события оценки рецензии `ReviewRating`
        broker: брокер сообщений

    Returns:
        Response: http ответ

    """
    await broker.post_review_rating(review_rating=review_rating)
    return Response(status_code=HTTPStatus.OK)

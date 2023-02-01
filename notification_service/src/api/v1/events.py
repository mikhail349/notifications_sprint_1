"""Модуль API-запросов событий."""

from http import HTTPStatus

from fastapi import APIRouter, Response

from src.api.v1.models.event import ReviewRatingEvent

router = APIRouter(prefix='/events', tags=['События'])


@router.post('/review_rating', summary='Событие оценки рецензии')
def post_review_rating(review_rating_event: ReviewRatingEvent) -> Response:
    """Отправить событие оценки рецензии.

    Args:
        review_rating_event: модель события оценки рецензии `ReviewRatingEvent`

    Returns:
        Response: http ответ

    """
    return Response(status_code=HTTPStatus.OK)

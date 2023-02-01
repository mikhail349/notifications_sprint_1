"""Модуль классов событий."""

import uuid

from pydantic import BaseModel


class ReviewRatingEvent(BaseModel):
    """Модель события оценки рецензии."""

    username: str
    review_id: uuid.UUID
    rating: int

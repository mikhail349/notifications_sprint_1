"""Модуль моделей событий рецензии."""
import datetime
import uuid

from pydantic import BaseModel, Field

from src.api.v1.models.base import Event


class ReviewRating(BaseModel):
    """Модель оценки рецензии."""

    username: str
    review_id: uuid.UUID
    rating: int = Field(ge=0, le=10)
    updated_at: datetime.datetime


class ReviewRatingEvent(Event):
    """Модель события оценки рецензии."""

    body: ReviewRating

"""Модуль классов событий."""
import datetime
import uuid

from pydantic import Field

from src.models.base import BaseModel


class ReviewRating(BaseModel):
    """Модель события оценки рецензии."""

    username: str
    review_id: uuid.UUID
    rating: int = Field(ge=0, le=10)
    updated_at: datetime.datetime

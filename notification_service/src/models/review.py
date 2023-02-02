"""Модуль классов событий."""
import uuid
import datetime

from pydantic import Field

from src.models.base import BaseModel 


class ReviewRating(BaseModel):
    """Модель события оценки рецензии."""

    username: str
    review_id: uuid.UUID
    rating: int = Field(ge=0, le=10)
    updated_at: datetime.datetime

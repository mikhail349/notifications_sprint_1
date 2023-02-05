"""Модуль моделей рецензии."""
import uuid

from pydantic import BaseModel

from src.storages.models.user import User


class Movie(BaseModel):
    """Модель фильма в рецензии."""

    name: str
    rating: float


class Review(BaseModel):
    """Модель рецензии фильма."""

    id: uuid.UUID
    movie: Movie
    author: User

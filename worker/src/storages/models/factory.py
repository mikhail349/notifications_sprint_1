"""Модул фабрики по производству объектов БД."""
import random
import uuid
from typing import Optional

from faker import Faker

from src.storages.models.review import Movie, Review
from src.storages.models.user import User

faker = Faker()

MAX_MOVIE_RATING = 10.0


def create_user(username: Optional[str] = None) -> User:
    """Создать рандомного пользователя.

    Args:
        username: имя пользователя. Если пусто - сгенерировать

    Returns:
        User: пользователь

    """
    return User(
        username=username or faker.simple_profile()['username'],
        name=faker.name(),
        email=faker.email(),
        phone_number=faker.phone_number(),
    )


def create_movie() -> Movie:
    """Создать рандомный фильм.

    Returns:
        Movie: фильм

    """
    return Movie(
        name=faker.word(),
        rating=random.uniform(0, MAX_MOVIE_RATING),
    )


def create_review(id: uuid.UUID) -> Review:  # noqa: WPS125
    """Создать радомную рецензи.

    Args:
        id: ИД рецензии

    Returns:
        Review: рецензия

    """
    movie = create_movie()
    author = create_user()
    return Review(
        id=id,
        movie=movie,
        author=author,
    )

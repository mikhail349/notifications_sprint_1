"""Модул фабрики по производству объектов БД."""
import random
import uuid
from typing import Optional

from faker import Faker

from src.storages.models.review import Movie, Review
from src.storages.models.user import User, UserNotificationSettings

faker = Faker()

MAX_MOVIE_RATING = 10.0


def create_random_id() -> uuid.UUID:
    """Создать рандомный ИД.

    Returns:
        UUID: ИД

    """
    return uuid.uuid4()


def create_user_notification_settings(
    allow_email: Optional[bool] = None,
) -> UserNotificationSettings:
    """Создать рандомные настройки уведомлений пользователя.

    Args:
        allow_email: получать email. Если None - сгенерировать

    Returns:
        UserNotificationSettings: настройки уведомлений пользователя

    """
    return UserNotificationSettings(
        allow_email=allow_email or random.choice([True, False]),
    )


def create_user(
    username: Optional[str] = None,
    email: Optional[str] = None,
) -> User:
    """Создать рандомного пользователя.

    Args:
        username: имя пользователя. Если None - сгенерировать
        email: эл. почта. Если None - сгенерировать

    Returns:
        User: пользователь

    """
    return User(
        username=username or faker.simple_profile()['username'],
        name=faker.name(),
        email=email or faker.email(),
        phone_number=faker.phone_number(),
        notification_settings=create_user_notification_settings(
            allow_email=True,
        ),
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

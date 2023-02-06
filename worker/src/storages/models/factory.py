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


def create_user_notification_settings() -> UserNotificationSettings:
    """Создать рандомные настройки уведомлений пользователя.

    Returns:
        UserNotificationSettings: настройки уведомлений пользователя

    """
    BOOL_CHOICES = [True, False]
    return UserNotificationSettings(
        allow_email=random.choice(BOOL_CHOICES),
        allow_sms=random.choice(BOOL_CHOICES)
    )

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
        notification_settings=create_user_notification_settings()
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

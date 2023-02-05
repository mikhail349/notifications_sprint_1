import random
import uuid
from typing import Optional

from faker import Faker

from src.storages.models.user import User
from src.storages.models.review import Movie, Review

faker = Faker()


def create_user(username: Optional[str] = None) -> User:
    return User(
        username=username or faker.simple_profile()["username"],
        name=faker.name(),
        email=faker.email(),
        phone_number=faker.phone_number()
    )


def create_movie() -> Movie:
    return Movie(
        name=faker.word(),
        rating=random.uniform(0., 10.)
    )


def create_review(id: uuid.UUID) -> Review:
    movie = create_movie()
    author = create_user()
    return Review(
        id=id,
        movie=movie,
        author=author
    )

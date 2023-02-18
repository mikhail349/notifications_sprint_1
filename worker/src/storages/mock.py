"""Модуль имитации хранилищ."""
import uuid
from typing import List, Tuple

from src.storages import base
from src.storages.models import factory
from src.storages.models.review import Review
from src.storages.models.user import User


class MockedDataStorage(base.DataStorage):
    """Класс имитации хранилища данных."""

    async def get_user(self, username: str) -> User:
        return factory.create_user(username=username)

    async def get_review(self, id: uuid.UUID) -> Review:
        return factory.create_review(id=id)

    async def get_users_by_cohort(self, cohort: str) -> List[User]:
        return [factory.create_user() for _ in range(3)]

    async def get_users(self, usernames: List[str]) -> List[User]:
        return [
            factory.create_user(username=username) for username in usernames
        ]

    async def login(self, username: str, password: str) -> Tuple[str, str]:
        return (
            'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImlzX3N1cGVydXNlciI6dHJ1ZSwicGVybWlzc2lvbnMiOltdfQ.RB0NoM1w4WEY3NUlvwzoCvoNb1Yse_KLQrdOUhs5hRcwb_94J2Z44AFnOicsEcDM6DyNQpuBVvTax6lhvRVFudOYCVrYOG-_aFS4AYHqpvcUQWTPiYpxYSM34mSQP1KzPkzGFUgIZmMwI1XdGnDfISfBHKvEnBlt8gZDEdvbENexhDRtQZj8zWmgJhgaJHt_gho8uuw8rJ1x8tCn3rwt7of6id-HcTGr4uqahihyiZSvqWBk4QJQBBwOy5NW6yDAqadmMEBGQbWATb8g-xhTNplm_UiKJH9-3VFCb2F703pxWV1BrOh7hHFyqhGHbj6mHojHBTi2HME7JieafqgF5fF4lG7A_ozL0pA8EjsVSIQ0sXhrF-8b-c-3tT3RTeCYFMg1ErziduYmIF5JsrVvBMI-xL7foJgPIlyTcLiczMWQN17WY0VVf0cOg1oo2Nv-ozM2OiSfvVKydjca8fXpZYVwllgP7WNFwolfwlSAvqy0cg6BgPQH-HQ65trywyA_li9iLHRwiUkg8TB2js1Vizjw0Gxru_NuhEVpQIH0__4C9svntBQZ-7ky9kjU1B4QDrRvJjeq-fal86hJrHdGcv1zNH614q0l9vS5AbVEKp5jcuILfkmeleShRp5CdulqOiSD1OsvWc446hGpTTunUhevZwlZ-IX91bMKngZ7AD8',  # noqa: E501
            '',
        )

"""Модуль имитации хранилищ."""
import uuid
from typing import Any, List

from src.models.notification import DeliveryType, EventType, Notification
from src.storages.base import DataStorage, NotificationStorage
from src.storages.models import factory
from src.storages.models.review import Review
from src.storages.models.user import User


class MockedDataStorage(DataStorage):
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


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища настроек уведомлений."""

    async def add_notification(self, notification: Notification) -> Any:
        return factory.create_random_id()

    async def get_template(
        self,
        delivery_type: DeliveryType,
        event_type: EventType,
    ) -> str:
        def get_email(event_type: EventType):  # noqa: WPS430
            emails = {
                EventType.USER_REGISTERED: """
                    <html>
                        <body>
                            <div>Приветствуем Вас, {{ user.name }}!</div>
                        </body>
                    </html>
                """,
                EventType.REVIEW_RATED: """
                    <html>
                        <body>
                            <div>
                                Вашу рецензию на фильм {{ review.movie.name }}
                                оценил пользователь {{ user.name }}
                            </div>
                        </body>
                    </html>
                """,
            }
            return emails[event_type]

        def get_sms(event_type: EventType):  # noqa: WPS430
            sms = {
                EventType.USER_REGISTERED: """
                    Приветствуем Вас, {{ user.name }}!
                """,
            }
            return sms[event_type]

        mapping = {
            DeliveryType.EMAIL: get_email,
            DeliveryType.SMS: get_sms,
        }
        return mapping[delivery_type](event_type)

    async def get_template_by_id(self, id: uuid.UUID) -> str:
        templates = {
            uuid.UUID('3fa85f64-5717-4562-b3fc-2c963f66afa6'): """
                Специально для вас, {{ user.name }}!
            """,
        }
        return templates[id]

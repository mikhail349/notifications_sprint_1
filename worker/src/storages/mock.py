"""Модуль имитации хранилищ."""
from typing import List
import uuid

from src.models.notification import DeliveryType, EventType
from src.storages.base import NotificationStorage, DataStorage
from src.storages.models.user import User
from src.storages.models.review import Review, Movie
from src.storages.models.factory import create_user, create_review


class MockedDataStorage(DataStorage):
    """Класс имитации хранилища данных."""

    async def get_user(self, username: str) -> User:
        return create_user(username=username)

    async def get_review(self, id: uuid.UUID) -> Review:
        return create_review(id=id)


class MockedNotificationStorage(NotificationStorage):
    """Класс имитации хранилища настроек уведомлений."""

    async def get_queues(self) -> List[str]:
        return ['low_priority', 'high_priority']

    async def get_sender_plugins(self) -> List[str]:
        return ['src.senders.email']
    
    async def get_handlers(self) -> List[str]:
        return ['src.handlers.user']
    
    async def get_handler(self, event_type: EventType) -> List[str]:
        mapping = {
            EventType.USER_REGISTERED: 'src.handlers.user',
        }
        return mapping[event_type]

    async def get_sender_plugin(
        self,
        delivery_type: DeliveryType,
    ) -> str:
        mapping = {
            DeliveryType.EMAIL: 'src.senders.email',
        }
        return mapping[delivery_type]

    async def get_template(
        self,
        delivery_type: DeliveryType,
        event_type: EventType
    ) -> str:
        def get_email(event_type: EventType):
            emails = {
                EventType.USER_REGISTERED: """
                    <html>
                        <body>
                            <div>Приветствуем Вас, {{name}}!</div>
                        </body>
                    </html>
                """,
                EventType.REVIEW_RATED: """
                    <html>
                        <body>
                            <div>
                                Вашу рецензию на фильм {{movie_name}}
                                оценил пользователь {{rater_name}}
                            </div>
                        </body>
                    </html>
                """
            }
            return emails[event_type]

        def get_sms(event_type: EventType):
            sms = {
                EventType.USER_REGISTERED: """
                    Приветствуем Вас, {{name}}!
                """
            }
            return sms[event_type]

        mapping = {
            DeliveryType.EMAIL: get_email,
            DeliveryType.SMS: get_sms
        }
        return mapping[delivery_type](event_type)

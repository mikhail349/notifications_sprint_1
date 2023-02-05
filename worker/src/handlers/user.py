from typing import Dict

from src.handlers import factory
from src.handlers.base import Handler
from src.models.notification import Notification
from src.storages.base import DataStorage


class UserHandler(Handler):

    def __init__(self, storage: DataStorage) -> None:
        self.storage = storage

    async def get_data(self, msg: Dict) -> Dict:
        recipient = await self.storage.get_user(username=msg["username"])
        payload = {
            "name": recipient.name
        }

        return {
            "email": recipient.email,
            "phone_number": recipient.phone_number,
            "payload": payload
        }


def initialize():
    factory.register('src.handlers.user', UserHandler)

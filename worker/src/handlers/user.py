from typing import Dict

from src.handlers import factory
from src.handlers.base import Handler
from src.models.notification import Notification
from src.storages.base import DataStorage


class UserHandler(Handler):

    async def get_data(self, msg_body: Dict) -> Dict:
        recipient = await self.storage.get_user(username=msg_body["username"])
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

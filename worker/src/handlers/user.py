"""Модуль обработчика событий пользователя."""
from src.handlers.base import EventHandler
from src.models.message import Message
from src.senders.base import Sender


class UserHandler(EventHandler):
    """Класс обработчика событий пользователя."""

    async def process(
        self,
        msg: Message,
        sender: Sender,
    ):
        recipient = await self.data_storage.get_user(
            username=msg.body['username'],
        )
        template = await self.notification_storage.get_template(
            delivery_type=msg.delivery_type,
            event_type=msg.event_type,
        )
        filled_template = self.templater.get_filled_template(
            template=template,
            template_data={'user': recipient},
        )
        await sender.send(recipient=recipient, text=filled_template)

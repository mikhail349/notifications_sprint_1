"""Модуль обработчика события регистрации пользователя."""
from src.handlers.base import EventHandler
from src.models.message import Message
from src.senders.base import Sender
from src.url_shorteners.base import URLShortenerMixin


class UserRegisteredHandler(URLShortenerMixin, EventHandler):
    """Класс обработчика события регистрации пользователя."""

    async def process(
        self,
        msg: Message,
        sender: Sender,
    ):
        short_url = self.url_shortener.shorten('https://auth/long_url')
        recipient = await self.data_storage.get_user(
            username=msg.body['username'],
        )
        template = await self.template_storage.get_template(
            delivery_type=msg.delivery_type,
            event_type=msg.event_type,
        )
        filled_template = self.templater.get_filled_template(
            template=template,
            template_data={
                'user': recipient,
                'link': {
                    'confirm_email': short_url,
                },
            },
        )
        await sender.send(recipient=recipient, text=filled_template)

"""Модуль обработчика события регистрации пользователя."""
from datetime import datetime, timedelta
from urllib import parse as urllib_parse

import jwt

from src.config.jwt import jwt_config
from src.handlers.base import EventHandler
from src.models.message import Message
from src.senders.base import Sender
from src.storages.base import URLType
from src.url_shorteners.base import URLShortenerMixin


class UserRegisteredHandler(URLShortenerMixin, EventHandler):
    """Класс обработчика события регистрации пользователя."""

    async def get_email_confirmation_url(self, username: str):
        confirm_email_url = await self.config_storage.get_url(
            url_type=URLType.CONFIRM_EMAIL_URL,
        )
        redirect_url = await self.config_storage.get_url(
            url_type=URLType.REDIRECT_URL,
        )
        payload = {
            'sub': username,
            'exp': datetime.now() + timedelta(seconds=jwt_config.expires),
        }
        token = jwt.encode(
            payload,
            jwt_config.secret,
            algorithm=jwt_config.algorithm,
        )
        return """
            {confirm_email_url}?token={token}&redirect_url={redirect_url}
        """.format(
            confirm_email_url=confirm_email_url,
            token=token,
            redirect_url=urllib_parse.quote(redirect_url),
        )

    async def process(
        self,
        msg: Message,
        sender: Sender,
    ):
        recipient = await self.data_storage.get_user(
            username=msg.body['username'],
        )
        confirm_email_url = await self.get_email_confirmation_url(
            username=recipient.username,
        )
        short_url = self.url_shortener.shorten(confirm_email_url)
        template = await self.config_storage.get_template(
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

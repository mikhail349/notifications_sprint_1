"""Моудль обработчика рассылок из админ панели."""
import uuid

from src.handlers import factory
from src.handlers.base import EventHandler
from src.models.notification import Notification
from src.senders.base import Sender


class AdminHandler(EventHandler):
    """Класс обработчика рассылок из админ панели."""

    async def process(
        self,
        msg: Notification,
        sender: Sender,
    ):
        recipients = await self.data_storage.get_users_by_cohort(
            cohort=msg.body['cohort'],
        )
        template = await self.notification_storage.get_template_by_id(
            id=uuid.UUID(msg.body['template_id']),
        )

        for recipient in recipients:
            filled_template = self.templater.get_filled_template(
                template=template,
                template_data={'user': recipient},
            )
            await sender.send(
                recipient=recipient,
                text=filled_template,
                subject=msg.body['subject'],
            )


def initialize():
    """Зарегистрировать модуль в фабрике."""
    factory.register('src.handlers.admin', AdminHandler)

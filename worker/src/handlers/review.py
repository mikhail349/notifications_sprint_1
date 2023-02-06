"""Модуль обработчика событий рецензии."""
from src.handlers.base import EventHandler
from src.models.notification import Notification
from src.senders.base import Sender


class ReviewHandler(EventHandler):
    """Класс обработчика событий рецензии."""

    async def process(
        self,
        msg: Notification,
        sender: Sender,
    ):
        user = await self.data_storage.get_user(username=msg.body['username'])
        review = await self.data_storage.get_review(id=msg.body['review_id'])
        template = await self.notification_storage.get_template(
            delivery_type=msg.delivery_type,
            event_type=msg.event_type,
        )
        filled_template = self.templater.get_filled_template(
            template=template,
            template_data={'user': user, 'review': review},
        )
        await sender.send(recipient=review.author, text=filled_template)

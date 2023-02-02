"""Модуль с абстрактным брокером сообщений."""
from abc import ABC, abstractmethod

from src.models.review import ReviewRating


class Broker(ABC):
    """Абстрактный класс брокера."""

    @abstractmethod
    async def post_review_rating(self, review_rating: ReviewRating) -> None:
        """Отправить сообщение об оценке рецензии.

        Args:
            review_rating: инстанс класса `ReviewRating`

        """

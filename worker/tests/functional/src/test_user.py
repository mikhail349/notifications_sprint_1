"""Модуль тестов событий пользователя."""
import pytest

from src.models.message import DeliveryType, EventType, Message


@pytest.mark.asyncio
async def test_registered(worker, email_sender):
    """Тест события регистрации пользователя."""
    USERNAME = 'ivan325'

    msg = Message(
        delivery_type=DeliveryType.EMAIL,
        event_type=EventType.USER_REGISTERED,
        body={
            'username': USERNAME,
        }
    )
    await worker.broker.send_message(msg)
    assert email_sender.last_email['recipient'].username == USERNAME

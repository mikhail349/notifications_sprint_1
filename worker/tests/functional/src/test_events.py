"""Модуль тестов событий пользователя."""
import uuid
from typing import Dict

import pytest

from src.models.message import DeliveryType, EventType, Message
from src.services.worker import Worker
from src.storages.mock import MockedDataStorage
from src.storages.models.notification import Status
from src.storages.models.factory import create_review
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.storages import MockedNotificationStorage


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'input_body, expected_status',
    [
        ({'username': 'ivan325'}, Status.SUCCESS),
        ({}, Status.ERROR),
    ],
)
async def test_user_registered(  # noqa: WPS211
    worker: Worker,
    broker: MockedBroker,
    email_sender: MockedEmailSender,
    notification_storage: MockedNotificationStorage,
    input_body: Dict,
    expected_status: Status,
):
    """Тест события регистрации пользователя.

    Args:
        worker: фикстура воркера
        broker: фикстура имитации брокера
        email_sender: фикстура имитации отправки email
        notification_storage: фикстура имитации хранилища уведомлений,
        input_body: тело сообщения для теста
        expected_status: ожидаемый статус уведомления

    """
    msg = Message(
        delivery_type=DeliveryType.EMAIL,
        event_type=EventType.USER_REGISTERED,
        body=input_body,
    )
    await broker.send_message(msg)

    notification = notification_storage.last_notification
    assert notification is not None and notification.status == expected_status

    if notification.status == Status.SUCCESS:
        recipient = email_sender.last_recipient
        assert (
            recipient is not None
            and recipient.username == input_body.get('username')
        )

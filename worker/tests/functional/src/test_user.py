"""Модуль тестов событий пользователя."""
from typing import Dict

import pytest

from src.models.message import DeliveryType, EventType, Message
from src.services.worker import Worker
from src.storages.models.notification import Status
from tests.functional.src.assertions import assert_response
from tests.functional.src.mocks import constants
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.storages import MockedNotificationStorage


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'input_body, expected_status',
    [
        ({'username': constants.USERNAME}, Status.SUCCESS),
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
    assert_response(
        email_sender=email_sender,
        notification_storage=notification_storage,
        expected_status=expected_status,
        successful_recipient_username=input_body.get('username', ''),
    )

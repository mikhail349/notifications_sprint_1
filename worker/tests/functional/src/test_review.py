"""Модуль тестов событий рецензии."""
from typing import Dict

import pytest

from src.models.message import DeliveryType, EventType, Message
from src.services.worker import Worker
from src.storages.models.notification import Status
from src.storages.models.review import Review
from tests.functional.src.assertions import assert_response
from tests.functional.src.mocks import constants
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.storages import MockedNotificationStorage


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'input_body, expected_status',
    [
        (
            {'username': constants.USERNAME, 'review_id': constants.REVIEW_ID},
            Status.SUCCESS,
        ),
        ({}, Status.ERROR),
    ],
)
async def test_review_rated(  # noqa: WPS211
    worker: Worker,
    broker: MockedBroker,
    email_sender: MockedEmailSender,
    notification_storage: MockedNotificationStorage,
    review: Review,
    input_body: Dict,
    expected_status: Status,
):
    """Тест события оценки ревью.

    Args:
        worker: фикстура воркера
        broker: фикстура имитации брокера
        email_sender: фикстура имитации отправки email
        notification_storage: фикстура имитации хранилища уведомлений
        review: фикстура резенции на фильм
        input_body: тело сообщения для теста
        expected_status: ожидаемый статус уведомления

    """
    msg = Message(
        delivery_type=DeliveryType.EMAIL,
        event_type=EventType.REVIEW_RATED,
        body=input_body,
    )
    await broker.send_message(msg)
    assert_response(
        email_sender=email_sender,
        notification_storage=notification_storage,
        expected_status=expected_status,
        successful_recipient_username=review.author.username,
    )

"""Модуль тестов событий из админ-панели."""
import uuid
from typing import Dict

import pytest

from src.models.message import DeliveryType, EventType, Message
from src.services.worker import Worker
from src.storages.models.notification import Status
from tests.functional.src.assertions import assert_response
from tests.functional.src.mocks import constants, storages
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'input_body, expected_status',
    [
        (
            {
                'cohort': constants.COHORT_NAME,
                'template_id': str(constants.TEMPLATE_ID),
                'subject': constants.SUBJECT,
            },
            Status.SUCCESS,
        ),
        (
            {
                'cohort': constants.COHORT_NAME,
            },
            Status.ERROR,
        ),
    ],
)
async def test_cohort(  # noqa: WPS211
    worker: Worker,
    broker: MockedBroker,
    email_sender: MockedEmailSender,
    notification_storage: storages.MockedNotificationStorage,
    data_storage: storages.MockedDataStorage,
    template: uuid.UUID,
    cohort: str,
    input_body: Dict,
    expected_status: Status,
):
    """Тест события рассылки по когорте.

    Args:
        worker: фикстура воркера
        broker: фикстура имитации брокера
        email_sender: фикстура имитации отправки email
        notification_storage: фикстура имитации хранилища уведомлений
        data_storage: фикстура имитации хранилища настроек
        template: фикстура шаблона
        cohort: фикстура когорты
        input_body: тело сообщения для теста
        expected_status: ожидаемый статус уведомления

    """
    msg = Message(
        delivery_type=DeliveryType.EMAIL,
        event_type=EventType.ADMIN,
        body=input_body,
    )
    await broker.send_message(msg)

    cohort_users = await data_storage.get_users_by_cohort(
        cohort=input_body['cohort'],
    )
    for user in cohort_users:
        assert_response(
            email_sender=email_sender,
            notification_storage=notification_storage,
            expected_status=expected_status,
            successful_recipient_username=user.username,
        )

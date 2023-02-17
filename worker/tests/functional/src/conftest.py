"""Модуль фикстур."""
import pytest
import pytest_asyncio

from src.handlers.user import UserRegisteredHandler
from src.handlers.review import ReviewHandler
from src.models.message import DeliveryType, EventType
from src.services.worker import Worker
from src.storages.mock import MockedDataStorage
from src.templaters.jinja import Jinja2Templater
from tests.functional.src.mocks import storages
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.url_shorteners import MockedURLShortener


@pytest.fixture
def broker():
    """Фикстура брокера.

    Returns:
        MockedBroker: класс брокера сообщений.

    """
    return MockedBroker()


@pytest.fixture
def email_sender():
    """Фикстура отправителя email.

    Returns:
        MockedEmailSender: класс отправителя email.

    """
    return MockedEmailSender()


@pytest.fixture
def notification_storage():
    """Фикстура хранилища уведомлений.

    Returns:
        MockedNotificationStorage: класс хранилища уведомлений.

    """
    return storages.MockedNotificationStorage()


@pytest.fixture
def data_storage():
    return MockedDataStorage()


@pytest_asyncio.fixture
async def worker(broker, email_sender, notification_storage, data_storage):
    """Фикстура воркера.

    Args:
        broker: фикстура брокера
        email_sender: фикстура отправителя email
        notification_storage: фикстура хранилища уведомлений

    Yields:
        worker

    """
    worker = Worker(broker=broker)
    worker.add_sender(DeliveryType.EMAIL, email_sender)
    worker.add_handler(
        EventType.USER_REGISTERED,
        UserRegisteredHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=storages.MockedConfigStorage(),
            templater=Jinja2Templater(),
            url_shortener=MockedURLShortener(),
        ),
    )
    worker.add_handler(
        EventType.REVIEW_RATED,
        ReviewHandler(
            data_storage=MockedDataStorage(),
            notification_storage=notification_storage,
            config_storage=storages.MockedConfigStorage(),
            templater=Jinja2Templater(),
        ),
    )
    await worker.run()
    yield worker

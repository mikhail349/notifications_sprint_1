"""Модуль фикстур."""
import pytest
import pytest_asyncio

from src.handlers.admin import AdminHandler
from src.handlers.review import ReviewHandler
from src.handlers.user import UserRegisteredHandler
from src.models.message import DeliveryType, EventType
from src.services.worker import Worker
from src.templaters.jinja import Jinja2Templater
from tests.functional.src.mocks import storages
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.url_shorteners import MockedURLShortener

pytest_plugins = (
    'tests.functional.fixtures.objects',
    'tests.functional.fixtures.storages',
)


@pytest.fixture
def broker() -> MockedBroker:
    """Фикстура брокера.

    Returns:
        MockedBroker: класс брокера сообщений.

    """
    return MockedBroker()


@pytest.fixture
def email_sender() -> MockedEmailSender:
    """Фикстура отправителя email.

    Returns:
        MockedEmailSender: класс отправителя email.

    """
    return MockedEmailSender()


@pytest_asyncio.fixture
async def worker(
    broker: MockedBroker,
    email_sender: MockedEmailSender,
    notification_storage: storages.MockedNotificationStorage,
    data_storage: storages.MockedDataStorage,
    config_storage: storages.MockedConfigStorage,
) -> Worker:
    """Фикстура воркера.

    Args:
        broker: фикстура брокера
        email_sender: фикстура отправителя email
        notification_storage: фикстура хранилища уведомлений
        data_storage: фикстура хранилища данных
        config_storage: фикстура хранилища настроек

    Returns:
        Worker: воркер

    """
    worker = Worker(broker=broker)
    worker.add_sender(DeliveryType.EMAIL, email_sender)
    worker.add_handler(
        EventType.USER_REGISTERED,
        UserRegisteredHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=config_storage,
            templater=Jinja2Templater(),
            url_shortener=MockedURLShortener(),
        ),
    )
    worker.add_handler(
        EventType.REVIEW_RATED,
        ReviewHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=config_storage,
            templater=Jinja2Templater(),
        ),
    )
    worker.add_handler(
        EventType.ADMIN,
        AdminHandler(
            data_storage=data_storage,
            notification_storage=notification_storage,
            config_storage=config_storage,
            templater=Jinja2Templater(),
        ),
    )
    await worker.run()
    return worker

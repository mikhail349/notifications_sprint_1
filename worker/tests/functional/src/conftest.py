import pytest
import pytest_asyncio

from src.models.message import DeliveryType, EventType
from src.handlers.user import UserRegisteredHandler
from src.services.worker import Worker
from src.storages.mock import MockedDataStorage
from src.templaters.jinja import Jinja2Templater
from tests.functional.src.mocks import storages
from tests.functional.src.mocks.brokers import MockedBroker
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.url_shorteners import MockedURLShortener


@pytest.fixture
def broker():
    return MockedBroker()


@pytest.fixture
def email_sender():
    return MockedEmailSender()


@pytest_asyncio.fixture
async def worker(broker, email_sender):
    worker = Worker(broker=broker)
    worker.add_sender(DeliveryType.EMAIL, email_sender)
    worker.add_handler(
        EventType.USER_REGISTERED,
        UserRegisteredHandler(
            data_storage=MockedDataStorage(),
            notification_storage=storages.MockedNotificationStorage(),
            config_storage=storages.MockedConfigStorage(),
            templater=Jinja2Templater(),
            url_shortener=MockedURLShortener(),
        ),
    )
    await worker.run()
    yield worker

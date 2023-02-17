from src.senders.base import Sender
from src.storages.models.user import User


class MockedEmailSender(Sender):

    def __init__(self) -> None:
        super().__init__()

    async def send(self, recipient: User, text: str, **options) -> None:
        self.last_email = {
            'recipient': recipient,
            'text': text,
            **options,
        }

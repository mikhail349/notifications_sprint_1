"""Вспомогательный модуль для проверки тестов."""
from src.storages.models.notification import Status
from tests.functional.src.mocks.senders import MockedEmailSender
from tests.functional.src.mocks.storages import MockedNotificationStorage


def assert_response(
    email_sender: MockedEmailSender,
    notification_storage: MockedNotificationStorage,
    expected_status: Status,
    successful_recipient_username: str,
):
    """Проверить результат обработки воркера.

    Args:
        email_sender: фикстура имитации отправки email
        notification_storage: фикстура имитации хранилища уведомлений
        expected_status: ожидаемый статус уведомления
        successful_recipient_username: имя пользователя получателя уведомления

    """
    notification = notification_storage.last_notification
    assert notification is not None and notification.status == expected_status

    is_username_emailed = email_sender.is_username_emailed(
        successful_recipient_username,
    )
    assert is_username_emailed == (notification.status == Status.SUCCESS)

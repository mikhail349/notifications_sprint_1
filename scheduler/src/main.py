"""Основной модуль планирощика рассылок."""
import http
import time

from dateutil.relativedelta import relativedelta
from src.config.api import APISettings
from src.config.postgresql import PSQLSettings
from src.delivery_api_client import DeliveryAPIClient
from src.models.mailing import AdminEvent, Periodicity
from src.storage.postgresql import PostgresStorage


def get_next_date(current_planed_date, periodicity):  # noqa: WPS231
    """Рассчитать следующую дату рассылки.

    Args:
        current_planed_date: текущая дата рассылки
        periodicity: периодичность рассылки

    Returns:
        дата следующей рассылки

    Raises:
        ValueError: некорректная периодичность
    """
    if periodicity == Periodicity.once.value:
        new_date = None
    elif periodicity == Periodicity.daily.value:
        new_date = current_planed_date + relativedelta(days=1)
    elif periodicity == Periodicity.weekly.value:
        new_date = current_planed_date + relativedelta(weeks=1)
    elif periodicity == Periodicity.monthly.value:
        new_date = current_planed_date + relativedelta(months=1)
    else:
        raise ValueError()
    return new_date


storage = PostgresStorage(PSQLSettings().dict())
api_client = DeliveryAPIClient(**APISettings().dict())

if __name__ == '__main__':
    while True:  # noqa: WPS457
        admin_events = storage.get_pending_notifications()

        for event in admin_events:
            admin_event = AdminEvent(**event)
            next_date = get_next_date(
                admin_event.next_planned_date,
                admin_event.periodicity.value,
            )

            response = api_client.send(
                delivery_type=admin_event.channel,
                cohort=admin_event.user_group,
                template_id=admin_event.template_id,
                subject=admin_event.subject,
            )
            if response.status_code == http.HTTPStatus.OK:
                storage.update_processed_notifications(
                    admin_event.id,
                    next_date,
                )
            time.sleep(1)

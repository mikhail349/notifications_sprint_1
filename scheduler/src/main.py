"""Основной модуль планирощика рассылок."""
import http
import logging
import time

from dateutil.relativedelta import relativedelta
from src.config.api import APISettings
from src.config.postgresql import PSQLSettings
from src.delivery_api_client import DeliveryAPIClient
from src.models.mailing import AdminEvent, Periodicity
from src.storage.postgresql import PostgresStorage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_next_date(current_planed_date, periodicity):  # noqa: WPS231
    """Рассчитать следующую дату рассылки.

    Args:
        current_planed_date: текущая дата рассылки
        periodicity: периодичность рассылки

    Returns:
        дата следующей рассылки
    """
    if periodicity == Periodicity.once.value:
        return None
    mapping = {
        Periodicity.daily.value: 'days',
        Periodicity.weekly.value: 'weeks',
        Periodicity.monthly.value: 'months',
    }
    kwargs = {mapping[periodicity]: 1}
    return current_planed_date + relativedelta(**kwargs)


storage = PostgresStorage(PSQLSettings().dict())
api_client = DeliveryAPIClient(**APISettings().dict())

if __name__ == '__main__':
    logger.info('Notifications scheduler is up and running')
    while True:  # noqa: WPS457
        admin_events = storage.get_pending_notifications()

        for event in admin_events:
            admin_event = AdminEvent(**event)
            next_date = get_next_date(
                admin_event.next_planned_date,
                admin_event.periodicity.value,
            )

            response = api_client.send(
                delivery_type=admin_event.channel.value,
                cohort=admin_event.user_group,
                template_id=admin_event.template_id,
                subject=admin_event.subject,
                priority=admin_event.priority.value,
            )
            if response.status_code == http.HTTPStatus.OK:
                storage.update_processed_notifications(
                    admin_event.id,
                    next_date,
                )
            time.sleep(1)

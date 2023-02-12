"""Модуль хранилища PostgreSQL."""
import uuid
from contextlib import contextmanager
from datetime import datetime
from typing import Dict

import backoff
import psycopg2
from psycopg2.extensions import connection
from psycopg2.extras import DictCursor, DictRow
from src.storage.base import Storage


class PostgresStorage(Storage):
    """Класс хранилища PostgreSQL."""

    def __init__(self, connection_data: Dict):
        """Инициализация класса.

        Args:
            connection_data: словарь с параметрами подключения
        """
        self.connection_data = connection_data

    @contextmanager
    def conn_context(self) -> connection:
        """Контекстный менеджер для подключения к бд.

        Yields:
            connection
        """
        conn = psycopg2.connect(
            **self.connection_data,
            cursor_factory=DictCursor,
        )
        yield conn
        conn.commit()
        conn.close()

    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def get_pending_notifications(self) -> DictRow:
        """Получить список рассылок с датой меньше или равной текуущей.

        Yields:
            DictRow

        """
        query = (
            'SELECT ns.id, ns.next_planned_date, ns.periodicity, ' +
            'ns.user_group, ns.template_id, nt.subject, nt.channel ' +
            'FROM notifications_scheduledmailing AS ns ' +
            'JOIN notifications_template AS nt ' +
            'ON ns.template_id = nt.id WHERE next_planned_date <= %s'
        )
        with self.conn_context() as conn:
            curs = conn.cursor()
            curs.execute(query, (datetime.now(),))
            while row := curs.fetchone():
                yield row

    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def update_processed_notifications(
        self,
        notification_id: uuid.UUID = None,
        next_date: datetime = None,
    ):
        """Обновить запланированную дату рассылки после отправки в очередь.

        Args:
            notification_id: идентификатор рассылки
            next_date: дата слудующей рассылки
        """
        next_date = str(next_date) if next_date else None
        query = (
            'UPDATE notifications_scheduledmailing ' +
            'SET next_planned_date = %s WHERE id = %s'
        )
        with self.conn_context() as conn:
            curs = conn.cursor()
            curs.execute(query, (next_date, str(notification_id)))

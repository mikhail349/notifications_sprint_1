"""Модуль клиента для взаимодействия с API рассылок."""

import logging

import backoff
import requests
from requests.exceptions import ConnectionError


class DeliveryAPIClient(object):
    """Класс клиента для взаимодействия с API рассылок."""

    def __init__(self, host, port):
        """Инициализация класса.

        Args:
            host: хост
            port: порт
        """
        self.host = host
        self.port = port
        self.admin_endpoint = '/api/v1/admin/'

    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def send(self, delivery_type, cohort, template_id, subject, priority):
        """Отправить запланированную рассылку на обработку.

        Args:
            delivery_type: способ рассылки
            cohort: группа юзеров
            template_id: идентефикатор шаблона
            subject: тема
            priority: приоритет

        Returns:
            requests.Response
        """
        body = {
            'delivery_type': delivery_type,
            'priority': priority,
            'body': {
                'cohort': cohort,
                'template_id': str(template_id),
                'subject': subject
            },
        }
        url = f'http://{self.host}:{self.port}{self.admin_endpoint}'
        try:
            return requests.post(url, json=body)
        except ConnectionError as err:
            logging.error('Trying to connect {url}.'.format(url=url))
            raise ConnectionError(err)

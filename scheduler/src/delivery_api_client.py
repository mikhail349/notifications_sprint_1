"""Модуль клиента для взаимодействия с API рассылок."""

import requests


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
        self.admin_endpoint = '/admin/'

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
                'template_id': template_id,
                'subject': subject,
            },
        }
        url = f'http://{self.host}:{self.port}{self.admin_endpoint}'
        return requests.post(url, data=body)

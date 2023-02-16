"""Модуль взаимодействия с хранилищем конфигураций в admin panel."""
import uuid

import aiohttp
from src.models.message import DeliveryType, EventType
from src.storages.base import ConfigStorage, URLType


class AdminPanelConfigurationStorage(ConfigStorage):
    """Класс для получения настроек, хранимых в сервисе админ-панели."""

    def __init__(self, api_url: str):
        """Инициализация.

        Args:
            api_url: url админ-панели
        """
        self.api_url = api_url
        self.templates_url = '{api}/templates/'.format(api=self.api_url)
        self.configs_url = '{api}/configs'.format(api=self.api_url)
        self.http_session = aiohttp.ClientSession()

    async def get_url(self, url_type: URLType) -> str:
        """Получить URL по ключу.

        Args:
            url_type: ключ URL

        Returns:
            str: URL

        """
        url = '{api}/configs/{value}'.format(
            api=self.api_url,
            value=url_type.value,
        )
        async with self.http_session.get(url) as res:
            res_data = await res.json()
            return res_data[url_type.value]

    async def get_template(
        self,
        delivery_type: DeliveryType,
        event_type: EventType,
    ) -> str:
        """Получить шаблон уведомления.

        Args:
            delivery_type: способ доставки
            event_type: тип события

        Returns:
            шаблон

        """
        url = self.templates_url
        params = {
            'event_type': event_type.value,
            'delivery_type': delivery_type.value,
        }
        async with self.http_session.get(url, params=params) as res:
            res_data = await res.json()
            return res_data['template']

    async def get_template_by_id(self, id: uuid.UUID) -> str:
        """Получить шаблон уведомления по ID.

        Args:
            id: ID шаблона уведомления

        Returns:
            str: шаблон

        """
        url = self.templates_url + str(id)
        async with self.http_session.get(url) as res:
            res_data = await res.json()
            return res_data['template']

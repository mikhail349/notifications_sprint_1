"""Модуль шаблонизатора Jinja2."""
from typing import Dict

from jinja2 import BaseLoader, Environment

from src.templaters.base import Templater


class Jinja2Templater(Templater):
    """Класс шаблонизатора Jinja2."""

    def __init__(self) -> None:
        """Инициализировать класс шаблонизатора Jinja2."""
        self.env = Environment(loader=BaseLoader(), autoescape=True)

    def get_filled_template(self, template: str, template_data: Dict) -> str:
        j_template = self.env.from_string(template)
        return j_template.render(template_data)

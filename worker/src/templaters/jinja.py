from typing import Dict

from jinja2 import Environment, BaseLoader

from src.templaters.base import Templater


class Jinja2Templater(Templater):
    """Класс шаблонизатора Jinja2."""

    def get_filled_template(self, template: str, data: Dict) -> str:
        j_template = Environment(loader=BaseLoader()).from_string(template)
        return j_template.render(data)

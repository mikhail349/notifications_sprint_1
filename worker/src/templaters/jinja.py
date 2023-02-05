from typing import Dict

from jinja2 import Environment, BaseLoader

from src.templaters.base import Templater
from src.models.notification import DeliveryType, EventType


class Jinja2Templater(Templater):
    """Класс шаблонизатора Jinja2."""

    async def get_template(
        self,
        delivery_type: DeliveryType,
        event_type: EventType
    ) -> str:
        def get_email(event_type: EventType):
            emails = {
                EventType.USER_REGISTERED: """
                    <html>
                        <body>
                            <div>Приветствуем Вас, {{name}}!</div>
                        </body>
                    </html>
                """,
                EventType.REVIEW_RATED: """
                    <html>
                        <body>
                            <div>
                                Вашу рецензию на фильм {{movie_name}}
                                оценил пользователь {{rater_name}}
                            </div>
                        </body>
                    </html>
                """
            }
            return emails[event_type]

        def get_sms(event_type: EventType):
            sms = {
                EventType.USER_REGISTERED: """
                    Приветствуем Вас, {{name}}!
                """
            }
            return sms[event_type]

        mapping = {
            DeliveryType.EMAIL: get_email,
            DeliveryType.SMS: get_sms
        }
        return mapping[delivery_type](event_type)

    def get_filled_template(self, template: str, data: Dict) -> str:
        j_template = Environment(loader=BaseLoader()).from_string(template)
        return j_template.render(data)

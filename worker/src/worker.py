from src.brokers.base import Broker


class Worker:
    """Класс обработчика событий.

    Args:
        broker: брокер сообщений `Broker`

    """

    def __init__(self, broker: Broker) -> None:
        """Инициализировать класс обработчика событий.

        Args:
            broker: брокер сообщений `Broker`

        """
        self.broker = broker

"""Module for Django application and its configuration."""
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """Class representing a Django application and its configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

"""Models for notifications admin panel app."""
import uuid

from django.db import models
from tinymce.models import HTMLField


class UUIDMixin(models.Model):
    """Mixin for id field."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:  # noqa: WPS306
        """Meta."""

        abstract = True


class Channel(models.TextChoices):
    """Possible choices for transfer channels."""

    email = 'email'
    websocket = 'websocket'


class UserGroup(models.TextChoices):
    """Possible choices for user groups."""

    all = 'all'


class Periodicity(models.TextChoices):
    """Possible choices for delivery periodicity."""

    once = 'once'
    daily = 'daily'
    weekly = 'weekly'
    monthly = 'monthly'


class Priority(models.TextChoices):
    """Possible choices for user priority."""

    low = 'low'
    high = 'high'


class Event(models.TextChoices):
    """Possible choices for events that trigger notification."""

    review_rated = 'review-reporting.v1.rated'
    user_registered = 'user-reporting.v1.registered'
    admin = 'admin-reporting.v1.event'


class Template(UUIDMixin):
    """Templates for notifications."""

    name = models.CharField('name', max_length=255)  # noqa: WPS432
    description = models.TextField('description', blank=True, null=True)
    channel = models.CharField(
        choices=Channel.choices,
        max_length=50,   # noqa: WPS432
    )
    subject = models.TextField(blank=True, null=True)
    template = HTMLField()
    event = models.CharField(
        choices=Event.choices,
        max_length=50,   # noqa: WPS432
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name.

        Returns:
            name
        """
        return self.name


class ScheduledMailing(UUIDMixin):
    """Models for scheduled mailings."""

    name = models.CharField('name', max_length=255)  # noqa: WPS432
    description = models.TextField('description', blank=True, null=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    template_params = models.TextField(
        'template_params',
        blank=True,
        null=True,
    )
    user_group = models.CharField(
        choices=UserGroup.choices,
        max_length=50,  # noqa: WPS432
    )
    is_instant = models.BooleanField()
    next_planned_date = models.DateTimeField(blank=True, null=True)
    periodicity = models.CharField(
        choices=Periodicity.choices,
        max_length=50,  # noqa: WPS432
    )
    priority = models.CharField(
        choices=Priority.choices,
        max_length=50,  # noqa: WPS432
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    last_processed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """Return name.

        Returns:
            name
        """
        return self.name


class Configuration(UUIDMixin):
    """Model to keep configurations for notifications."""

    name = models.SlugField('name', max_length=255)  # noqa: WPS432
    config_value = models.CharField('value', max_length=255)  # noqa: WPS432
    description = models.TextField('description', blank=True, null=True)

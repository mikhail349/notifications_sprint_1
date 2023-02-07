"""Administration panel."""
from django.contrib import admin
from notifications import models


@admin.register(models.Template)
class TemplatesAdmin(admin.ModelAdmin):
    """Admin interface for Template."""

    search_fields = ['name']


@admin.register(models.ScheduledMailing)
class ScheduledMailingsAdmin(admin.ModelAdmin):
    """Admin interface for Scheduled Mailing."""

    search_fields = ['name']

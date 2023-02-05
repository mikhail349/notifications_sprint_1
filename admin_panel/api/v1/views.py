"""Notifications admin api."""

import uuid

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from notifications.models import Template


@require_http_methods(['GET'])
def get_template(request: WSGIRequest, template_id: uuid.UUID) -> JsonResponse:
    """Возвращает шаблон сообщения по заданному uuid.

    Args:
        request: объект запроса
        template_id: идентификатор шаблона

    Returns:
        JsonResponse
    """
    tmpl = get_object_or_404(Template, id=template_id)
    return JsonResponse({'template': tmpl.template})

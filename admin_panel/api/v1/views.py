"""Notifications admin api."""

import uuid

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from notifications.models import Configuration, Template


@require_http_methods(['GET'])
def get_template_by_id(
    request: WSGIRequest,
    template_id: uuid.UUID,
) -> JsonResponse:
    """Возвращает шаблон сообщения по заданному uuid.

    Args:
        request: объект запроса
        template_id: идентификатор шаблона

    Returns:
        JsonResponse
    """
    tmpl = get_object_or_404(Template, id=template_id)
    return JsonResponse({'template': tmpl.template})


@require_http_methods(['GET'])
def get_template(request: WSGIRequest) -> JsonResponse:
    """Возвращает шаблон сообщения по заданным параметрам.

    Args:
        request: объект запроса

    Returns:
        JsonResponse
    """
    event_type = request.GET.get('event_type')
    delivery_type = request.GET.get('delivery_type')
    tmpl = get_object_or_404(Template, channel=delivery_type, event=event_type)
    return JsonResponse({'template': tmpl.template})


@require_http_methods(['GET'])
def get_config_value(request: WSGIRequest, config_name: str) -> JsonResponse:
    """Возвращает значение настройки по ее имени.

    Args:
        request: объект запроса
        config_name: название настройки

    Returns:
        JsonResponse
    """
    config_value = get_object_or_404(
        Configuration,
        name=config_name,
    ).config_value
    return JsonResponse({config_name: config_value})

"""API v1 routing."""
from django.urls import path

from api.v1 import views

urlpatterns = [
    path('templates/<uuid:template_id>/', views.get_template),
]

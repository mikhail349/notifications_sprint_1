"""API v1 routing."""
from api.v1 import views
from django.urls import path

urlpatterns = [
    path('templates/<uuid:template_id>/', views.get_template),
    path('configs/<str:config_name>/', views.get_config_value),
]

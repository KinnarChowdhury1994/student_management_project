from django.urls import path
from .views import healthCheck

urlpatterns = [
    path('enabled', healthCheck),
]
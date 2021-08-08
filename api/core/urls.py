from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DishViewSet

resources = DefaultRouter()
resources.register(r'menu', DishViewSet)

urlpatterns = resources.urls

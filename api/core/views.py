from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serialyzers import *


class DishViewSet(ModelViewSet):
    """Request the list of items offered by the restaurant"""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer

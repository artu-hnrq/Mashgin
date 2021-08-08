from rest_framework import serializers

from .models import *


class DishSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField()

    class Meta:
        model = Dish
        exclude = ('image_id',)

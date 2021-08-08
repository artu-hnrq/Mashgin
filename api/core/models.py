from django.conf import settings
from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=50)
    image_id = models.CharField(max_length=50)

    @property
    def image_url(self):
        return f'{settings.MEDIA_URL}{self.image_id}.jpg'

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(Resource):

    @property
    def count_dishes(self):
        return self.dish_set.count()

    class Meta:
        verbose_name_plural = "categories"


class Dish(Resource):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = "dishes"

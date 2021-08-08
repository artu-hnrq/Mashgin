from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_dishes')

    def count_dishes(self, obj):
        return f'{obj.count_dishes} dish(es)'


@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

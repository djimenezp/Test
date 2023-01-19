# Register your models here.
from django.contrib import admin

from app import models


class Default(admin.ModelAdmin):
    """
    Default model admin class
    """
    pass


@admin.register(models.Item)
class ItemAdmin(Default):
    list_display = ['__str__', 'color', 'status']
    list_editable = ['status']


@admin.register(models.Color)
class ColorAdmin(Default):
    list_display = ['color']


@admin.register(models.Status)
class StatusAdmin(Default):
    list_display = ['description']

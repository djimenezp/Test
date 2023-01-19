# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")


class Color(models.Model):
    color = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class Item(models.Model):
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    color = models.ForeignKey('Color', models.CASCADE, 'items')
    status = models.ForeignKey('Status', models.CASCADE, 'items')

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

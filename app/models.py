# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


class Default(models.Model):
    """
    Default abstact model class
    """

    class Meta:
        abstract = True


class Status(Default):
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    def __str__(self):
        return f"{self.id}-{self.description.capitalize()}"


class Color(Default):
    color = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return f"{self.id}-{self.color.capitalize()}"


class Item(Default):
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    color = models.ForeignKey('Color', models.CASCADE, 'items')
    status = models.ForeignKey('Status', models.CASCADE, 'items')

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return f"{self.id}-{self.description.capitalize()}-{self.brand.capitalize()}"

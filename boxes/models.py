from django.db import models

from containers import settings
from geo.models import Station


class ContainerType(models.Model):
    title = models.CharField(verbose_name="название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "тип контейнера"
        verbose_name_plural = "типы контейнеров"


# Create your models here.
class FreeContainer(models.Model):
    type = models.ForeignKey(ContainerType, models.CASCADE, verbose_name="тип")
    location = models.ForeignKey(Station, models.CASCADE, verbose_name="располжене")
    address = models.TextField(verbose_name="адрес", blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name="количество")
    parts = models.BooleanField(verbose_name="можно частями", default=True)
    date_from = models.DateField(verbose_name="свободны с")
    date_till = models.DateField(verbose_name="свободны до", null=True, blank=True)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)

    def __str__(self):
        if self.address:
            return "{} контейнеров с {} по адресу".format(self.count, self.date_from, self.address)
        else:
            return "{} контейнеров с {}".format(self.count, self.date_from)

    class Meta:
        verbose_name = "тип контейнера"
        verbose_name_plural = "типы контейнеров"


class NeededContainer(models.Model):
    type = models.ForeignKey(ContainerType, models.CASCADE, verbose_name="тип")
    location = models.ForeignKey(Station, models.CASCADE, verbose_name="располжене")
    address = models.TextField(verbose_name="адрес", blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name="количество")
    date_from = models.DateField(verbose_name="свободны с")
    date_till = models.DateField(verbose_name="свободны до", null=True, blank=True)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)

    def __str__(self):
        if self.address:
            return "{} контейнеров с {} по адресу".format(self.count, self.date_from, self.address)
        else:
            return "{} контейнеров с {}".format(self.count, self.date_from)

    class Meta:
        verbose_name = "тип контейнера"
        verbose_name_plural = "типы контейнеров"

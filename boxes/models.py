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
class BaseContainer(models.Model):
    """
    Базовый класс хранения информации о партии контейнеров
    """
    type = models.ForeignKey(ContainerType, models.CASCADE, verbose_name="тип")
    location = models.ForeignKey(Station, models.CASCADE, verbose_name="расположение")
    address = models.TextField(verbose_name="адрес", blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name="количество")
    date_from = models.DateField(verbose_name="свободны с")
    date_till = models.DateField(verbose_name="свободны до", null=True, blank=True)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)

    def __str__(self):
        location = "{} {} {}".format(self.location.title, self.location.city.title, self.location.city.region.title)
        if self.address:
            return "{} {} контейнеров с {} по адресу {}".format(location, self.count, self.date_from, self.address)
        else:
            return "{} {} контейнеров с {}".format(location, self.count, self.date_from)

    class Meta:
        abstract = True


class FreeContainer(BaseContainer):
    parts = models.BooleanField(verbose_name="можно частями", default=True)

    class Meta:
        verbose_name = "свободный контейнер"
        verbose_name_plural = "свободные контейнеры"


class NeededContainer(BaseContainer):
    class Meta:
        verbose_name = "искомый контейнер"
        verbose_name_plural = "искомые контейнеры"


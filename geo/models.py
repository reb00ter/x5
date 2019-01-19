from django.db import models


# Create your models here.
class Region(models.Model):
    title = models.CharField(verbose_name="название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "регион"
        verbose_name_plural = "регионы"


class City(models.Model):
    title = models.CharField(verbose_name="название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"


class Station(models.Model):
    title = models.CharField(verbose_name="название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "станция"
        verbose_name_plural = "станции"


from django.db import models

# Create your models here.
from core.models import User
from geo.models import Station, City, Region
from boxes.models import ContainerType, FreeContainer, NeededContainer
from boxes.filters import FreeContainerFilter


class BaseContainerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь", blank=True)
    date_from = models.DateField(verbose_name="с", null=True, blank=True)
    date_till = models.DateField(verbose_name="по", null=True, blank=True)
    type = models.ForeignKey(ContainerType, on_delete=models.CASCADE, verbose_name="тип контейнера")
    location = models.ManyToManyField(Station, verbose_name="станции", blank=True)
    location_city = models.ManyToManyField(City, verbose_name="города", blank=True)
    location_city_region = models.ManyToManyField(Region, verbose_name="регионы", blank=True)
    count = models.PositiveIntegerField(verbose_name="количество", default=1)
    address = models.CharField(verbose_name="адрес", max_length=255, null=True, blank=True)
    created = models.DateField(verbose_name="создан", auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name="активен")

    class Meta:
        abstract = True

    def __str__(self):
        return "{} от {}".format(self.user.email, self.created)

    def filter_dict(self):
        return {
            'date_from': self.date_from.strftime("%Y-%m-%d") if self.date_from else None,
            'date_till': self.date_till.strftime("%Y-%m-%d") if self.date_till else None,
            'type': self.type_id,
            'location': list(self.location.all().values_list('id', flat=True)),
            'location__city': list(self.location_city.all().values_list('id', flat=True)),
            'location__city__region': list(self.location_city_region.all().values_list('id', flat=True)),
            'count': self.count,
            'address': self.address
        }


class FreeContainerRequest(BaseContainerRequest):
    def containers(self):
        return FreeContainerFilter(self.filter_dict(), queryset=FreeContainer.objects.all())

from django.db import models
from django.db.models import Q
from django_filters import rest_framework as filters
from .models import BaseContainer, FreeContainer
from geo.models import Station, City, Region


class NumberInFilter(filters.ModelMultipleChoiceFilter):
    pass


class BaseContainerFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="date_from", lookup_expr='lte')
    date_till = filters.DateFilter(field_name="date_till", lookup_expr='gte')
    type = filters.NumberFilter(field_name='type')
    location = NumberInFilter(to_field_name='id', queryset=Station.objects.all())
    location__city = NumberInFilter(to_field_name='id', queryset=City.objects.all())
    location__city__region = NumberInFilter(to_field_name='id', queryset=Region.objects.all())
    count = filters.NumberFilter(field_name='count')
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')

    class Meta:
        models = BaseContainer
        fields = ['type', 'address', 'location', 'location__city', 'location__city__region', 'date_from', 'date_till',
                  'count']


class FreeContainerFilter(BaseContainerFilter):
    def filter_queryset(self, queryset):
        """
        Тут обрабатываем все нюансы фильтрации:
        собираем все location-штуки, учитываем возможность (или невозможность) взять только часть контейнеров
        """
        location_q = Q()
        count_q = Q()
        date_from_q = Q()
        date_till_q = Q()
        for name in self.form.data:
            value = self.form.data[name]
            if "location" in name and value is not None:
                # собираем всё про location по ИЛИ
                value = self.form.cleaned_data.get(name)
                if value.count() > 0:
                    lookup = '%s__%s' % (name, "in")
                    location_q = location_q | Q(**{lookup: value})
            elif name == "count":
                # для количества обрщаем внимание на то, что могут быть партии, которые можно взять не полностью
                count_q = (Q(count=value) & Q(parts=False)) | (Q(count__gte=value) & Q(parts=True))
            elif name == "date_from" and value is not None:
                # дата начала, конечно, должна быть больше либо равно чем у предложения,
                # но и меньше даты окончания предложения (если такая есть)
                date_from_q = (Q(date_from__lte=value) & Q(date_till__isnull=True)) | \
                              (Q(date_from__lte=value) & Q(date_till__gte=value))
            elif name == "date_till" and value is not None:
                # дата окончания больше
                date_till_q = Q(date_till__gte=value)
            else:
                # стандартный механизм по "И"
                queryset = self.filters[name].filter(queryset, value)
            assert isinstance(queryset, models.QuerySet), \
                "Expected '%s.%s' to return a QuerySet, but got a %s instead." \
                % (type(self).__name__, name, type(queryset).__name__)
        # применяем собранные фильры по количеству и расположению
        return queryset.filter(location_q).filter(count_q).filter(date_from_q).filter(date_till_q)

    class Meta:
        models = FreeContainer
        fields = ['type', 'address', 'location', 'location__city', 'location__city__region', 'date_from', 'date_till',
                  'count']

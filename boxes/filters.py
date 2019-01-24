from django_filters import rest_framework as filters
from .models import BaseContainer


class ContainerFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="date_from", lookup_expr='lte')
    date_till = filters.DateFilter(field_name="date_till", lookup_expr='gte')
    type = filters.NumberFilter(field_name='type')
    location = filters.NumberFilter(field_name='location')
    location__city = filters.NumberFilter(field_name='location__city')
    location__city__region = filters.NumberFilter(field_name='location__city__region')

    class Meta:
        models = BaseContainer
        fields = ['type', 'address', 'location', 'location__city', 'location__city__region', 'date_from', 'date_till']

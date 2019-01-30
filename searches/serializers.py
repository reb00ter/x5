
from rest_framework import serializers

from boxes.serializers import FreeContainerSerializer
from .models import FreeContainerRequest


class FreeContainerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeContainerRequest
        fields = ('id', 'created', 'user', 'type', 'location', 'location_city', 'location_city_region', 'address',
                  'count', 'date_from', 'date_till')


class FreeContainerResultsSerializer(serializers.ModelSerializer):
    search_results = serializers.SerializerMethodField()

    def get_search_results(self, obj):
        objs = obj.containers().qs
        return [FreeContainerSerializer(container).data for container in objs]

    class Meta:
        model = FreeContainerRequest
        fields = ('id', 'created', 'user', 'type', 'location', 'location_city', 'location_city_region', 'address',
                  'count', 'date_from', 'date_till', 'search_results')

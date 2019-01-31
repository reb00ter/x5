
from rest_framework import serializers

from boxes.serializers import FreeContainerSerializer
from .models import FreeContainerRequest


class FreeContainerRequestSerializer(serializers.ModelSerializer):
    type_title = serializers.SerializerMethodField()

    def get_type_title(self, obj):
        return obj.type.title

    class Meta:
        model = FreeContainerRequest
        fields = ('id', 'created', 'user', 'type', 'type_title', 'location', 'location_city', 'location_city_region',
                  'address', 'count', 'date_from', 'date_till')


class FreeContainerResultsSerializer(serializers.ModelSerializer):
    search_results = serializers.SerializerMethodField()
    type_title = serializers.SerializerMethodField()

    def get_search_results(self, obj):
        objs = obj.containers().qs
        return [FreeContainerSerializer(container).data for container in objs]

    def get_type_title(self, obj):
        return obj.type.title

    class Meta:
        model = FreeContainerRequest
        fields = ('id', 'created', 'user', 'type', 'type_title', 'location', 'location_city', 'location_city_region',
                  'address', 'count', 'date_from', 'date_till', 'search_results')

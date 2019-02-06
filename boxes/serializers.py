
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from boxes.models import FreeContainer, NeededContainer, ContainerType
from geo.serializers import StationStringSerializer


class ContainerTypeStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerType
        fields = ('title', )


class FreeContainerSerializer(serializers.ModelSerializer):
    type_title = serializers.SerializerMethodField()

    def get_type_title(self, obj):
        return obj.type.title

    location_data = serializers.SerializerMethodField()

    def get_location_data(self, obj):
        return StationStringSerializer(obj.location).data

    class Meta:
        model = FreeContainer
        fields = ('id', 'type', 'type_title', 'location', 'location_data', 'address', 'count', 'parts', 'date_from',
                  'date_till', 'price', 'contact')


class NeededContainerSerializer(serializers.ModelSerializer):
    type_title = serializers.SerializerMethodField()

    def get_type_title(self, obj):
        return obj.type.title

    location_data = serializers.SerializerMethodField()

    def get_location_data(self, obj):
        return StationStringSerializer(obj.location).data

    class Meta:
        model = NeededContainer
        fields = ('id', 'type', 'type_title', 'location', 'location_data', 'address', 'count', 'date_from',
                  'date_till', 'contact')


class ContainerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerType
        fields = ('id', 'title')

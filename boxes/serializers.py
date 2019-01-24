
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from boxes.models import FreeContainer, NeededContainer, ContainerType
from geo.serializers import StationStringSerializer


class ContainerTypeStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerType
        fields = ('title', )


class FreeContainerSerializer(serializers.ModelSerializer):
    type = StringRelatedField()
    location = StationStringSerializer()

    class Meta:
        model = FreeContainer
        fields = ('id', 'type', 'location', 'address', 'count', 'parts', 'date_from', 'date_till', 'contact')


class NeededContainerSerializer(serializers.ModelSerializer):
    type = StringRelatedField()
    location = StationStringSerializer(read_only=True)

    class Meta:
        model = NeededContainer
        fields = ('id', 'type', 'location', 'address', 'count', 'date_from', 'date_till', 'contact')


class ContainerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerType
        fields = ('id', 'title')

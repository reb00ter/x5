
from rest_framework import serializers

from boxes.models import FreeContainer, NeededContainer, ContainerType


class FreeContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeContainer
        fields = ('type', 'location', 'address', 'count', 'parts', 'date_from', 'date_till', 'contact')


class NeededContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeededContainer
        fields = ('type', 'location', 'address', 'count', 'date_from', 'date_till', 'contact')


class ContainerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerType
        fields = ('id', 'title')

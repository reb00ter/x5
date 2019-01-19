
from rest_framework import serializers

from boxes.models import FreeContainer, NeededContainer


class FreeContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FreeContainer
        fields = ('url', 'username', 'email', 'groups')


class NeededContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NeededContainer
        fields = ('url', 'name')

from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Station, City, Region


class RegionStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('title', )


class CityStringSerializer(serializers.ModelSerializer):
    region = StringRelatedField()

    class Meta:
        model = Station
        fields = ('title', 'region')


class StationStringSerializer(serializers.ModelSerializer):
    city = CityStringSerializer(read_only=True)

    class Meta:
        model = Station
        fields = ('id', 'title', 'city')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'title')


class CitySerializer(serializers.ModelSerializer):
    children = StationSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'title', 'children')

    def to_representation(self, instance):
        data = super(CitySerializer, self).to_representation(instance)
        data['opened'] = False
        data['visible'] = False
        return data


class RegionSerializer(serializers.ModelSerializer):
    children = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ('id', 'title', 'children')

    def to_representation(self, instance):
        data = super(RegionSerializer, self).to_representation(instance)
        data['opened'] = False
        data['visible'] = False
        return data

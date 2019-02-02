from rest_framework import serializers

from containers import settings


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

    def to_representation(self, instance):
        if instance.is_authenticated:
            return super(UserSerializer, self).to_representation(instance)
        return {'email': ""}

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


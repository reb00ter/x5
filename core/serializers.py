from rest_framework import serializers

from containers import settings
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # def to_representation(self, instance):
    #     if instance.is_authenticated:
    #         return super(UserSerializer, self).to_representation(instance)
    #     return {'email': ""}

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = User
        exclude = ['password', ]


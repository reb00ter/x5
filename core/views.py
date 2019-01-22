from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from containers import settings
from core.models import User
from core.serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

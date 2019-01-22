from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from boxes.models import NeededContainer, FreeContainer, ContainerType
from boxes.serializers import NeededContainerSerializer, FreeContainerSerializer, ContainerTypeSerializer


class ContainerTypeViewSet(viewsets.ModelViewSet):
    queryset = ContainerType.objects.all()
    serializer_class = ContainerTypeSerializer


class FreeContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FreeContainer.objects.all()
    serializer_class = FreeContainerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)


class NeededContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NeededContainer.objects.all()
    serializer_class = NeededContainerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

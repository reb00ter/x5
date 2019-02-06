from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly

from boxes.filters import FreeContainerFilter, NeedContainerFilter
from boxes.models import NeededContainer, FreeContainer, ContainerType
from boxes.serializers import NeededContainerSerializer, FreeContainerSerializer, ContainerTypeSerializer


class ContainerTypeViewSet(viewsets.ModelViewSet):
    queryset = ContainerType.objects.all()
    serializer_class = ContainerTypeSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class FreeContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FreeContainer.objects.all()
    serializer_class = FreeContainerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = FreeContainerFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(contact=self.request.user)


class NeededContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NeededContainer.objects.all()
    serializer_class = NeededContainerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = NeedContainerFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(contact=self.request.user)

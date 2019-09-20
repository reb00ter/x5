from django.http import HttpResponseForbidden

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly

from boxes.filters import FreeContainerFilter, NeedContainerFilter
from boxes.models import NeededContainer, FreeContainer, ContainerType
from boxes.serializers import NeededContainerSerializer, FreeContainerSerializer, ContainerTypeSerializer


class ContainerTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContainerType.objects.all()
    serializer_class = ContainerTypeSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class OwnersWritableModelViewSet(viewsets.ModelViewSet):
    """
    Base class for deny write access to foreign objects
    """
    def update(self, request, *args, **kwargs):
        """
        check access on update
        """
        instance = self.get_object()
        if self.request.user.is_superuser or instance.owner == self.request.user:
            return super(OwnersWritableModelViewSet, self).update(request, *args, **kwargs)
        return HttpResponseForbidden("Only owner or superuser can change object")

    def destroy(self, request, *args, **kwargs):
        """
        check access on destroy
        """
        instance = self.get_object()
        if self.request.user.is_superuser or instance.owner == self.request.user:
            return super(OwnersWritableModelViewSet, self).destroy(request, *args, **kwargs)
        return HttpResponseForbidden("Only owner or superuser can destroy object")

    def perform_create(self, serializer):
        """
        set current user as owner on create
        """
        serializer.save(owner=self.request.user)


class FreeContainerViewSet(OwnersWritableModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FreeContainer.objects.all()
    serializer_class = FreeContainerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = FreeContainerFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)


class NeededContainerViewSet(OwnersWritableModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NeededContainer.objects.all()
    serializer_class = NeededContainerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = NeedContainerFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)


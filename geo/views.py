from rest_framework import viewsets
from .models import Region, Station
from .serializers import RegionSerializer, StationSerializer


class RegionsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class StationsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer

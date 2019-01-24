from rest_framework import viewsets
from .models import Region
from .serializers import RegionSerializer


class RegionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

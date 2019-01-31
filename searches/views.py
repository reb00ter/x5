from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from boxes.serializers import FreeContainerSerializer
from .models import FreeContainerRequest
from .serializers import FreeContainerRequestSerializer, FreeContainerResultsSerializer


# Create your views here.
class FreeContainersRequestsViewSet(viewsets.ModelViewSet):
    detail_serializer_class = FreeContainerResultsSerializer
    serializer_class = FreeContainerRequestSerializer

    def get_queryset(self):
        """
        Возвращаем только поисковые запросы, созданные авторизованным пользователем
        """
        user = self.request.user
        return FreeContainerRequest.objects.filter(user=user, active=True).\
            prefetch_related('user', 'location', 'location_city', 'location_city_region')

    @action(detail=True)
    def results(self, request, pk=None):
        """
        Возвращает результаты поиска по этому фильтру на странице /api/search/free/<pk>/results
        """
        if pk is None:
            return Response([])
        obj = get_object_or_404(FreeContainerRequest, pk=pk)
        if obj.user != request.user:
            raise Http404
        objs = obj.containers().qs
        return Response([FreeContainerSerializer(container).data for container in objs])

    def perform_create(self, serializer):
        """
        Автоматически сохраняем пользователя
        """
        serializer.save(user=self.request.user)

"""containers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView, RedirectView
from core import views as core
from geo import views as geo
from boxes import views as boxes
from searches import views as search
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', core.UserViewSet)
router.register(r'locations', geo.RegionsViewSet)
router.register(r'containers/types', boxes.ContainerTypeViewSet)
router.register(r'containers/free', boxes.FreeContainerViewSet)
router.register(r'containers/needed', boxes.NeededContainerViewSet)
router.register(r'search/free', search.FreeContainersRequestsViewSet, basename='search_free')
# router.register(r'search/needed', search.NeededContainerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('api/', include(router.urls)),
    path('accounts/profile/', RedirectView.as_view(url=reverse_lazy('index')), name='profile'),
    path('', TemplateView.as_view(template_name="index.html"), name='index')
]

from django.contrib import admin
from .models import ContainerType, FreeContainer, NeededContainer

# Register your models here.
admin.site.register(ContainerType)
admin.site.register(FreeContainer)
admin.site.register(NeededContainer)

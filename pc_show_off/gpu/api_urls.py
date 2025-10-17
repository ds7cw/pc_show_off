from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import GpuViewSet

router = DefaultRouter()
router.register(r'', GpuViewSet, basename='gpu-api')

urlpatterns = [
    path('', include(router.urls)),
]

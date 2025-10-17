from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CpuViewSet

router = DefaultRouter()
router.register(r'', CpuViewSet, basename='cpu-api')

urlpatterns = [
    path('', include(router.urls)),
]

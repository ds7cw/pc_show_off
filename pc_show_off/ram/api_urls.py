from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RamViewSet

router = DefaultRouter()
router.register(r'', RamViewSet, basename='ram-api')

urlpatterns = [
    path('', include(router.urls)),
]

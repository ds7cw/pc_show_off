from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StorageViewSet

router = DefaultRouter()
router.register(r'', StorageViewSet, basename='storage-api')

urlpatterns = [
    path('', include(router.urls)),
]

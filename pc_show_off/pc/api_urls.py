from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import PcViewSet

router = DefaultRouter()
router.register(r'', PcViewSet, basename='pc')

urlpatterns = [
    path('', include(router.urls)),
]

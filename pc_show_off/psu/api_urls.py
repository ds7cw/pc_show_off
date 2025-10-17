from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import PsuViewSet

router = DefaultRouter()
router.register(r'', PsuViewSet, basename='psu-api')

urlpatterns = [
    path('', include(router.urls)),
]

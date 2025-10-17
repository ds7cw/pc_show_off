from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import MoboViewSet

router = DefaultRouter()
router.register(r'', MoboViewSet, basename='mobo-api')

urlpatterns = [
    path('', include(router.urls)),
]

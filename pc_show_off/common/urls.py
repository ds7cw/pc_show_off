from django.urls import path, include
from .views import index, components_library

urlpatterns = [
    path('', index, name='index-page'),
    path('components-library/', components_library, name='components-library'),
]
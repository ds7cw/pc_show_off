from django.urls import path, include
from .views import index, components_library, contributors

urlpatterns = [
    path('', index, name='index-page'),
    path('components-library/', components_library, name='components-library'),
    path('contributors/', contributors, name='contributors'),
]
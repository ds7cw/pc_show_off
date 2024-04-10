from django.urls import path, include
from .views import gpu_create, gpu_edit, gpu_delete, GpuDetailView, GpuListView


urlpatterns = [
    path('create/', gpu_create, name='gpu-create'),
    path('<int:gpu_id>/', include(
        [
            # path('details/', gpu_details, name='gpu-details'),
            path('details/', GpuDetailView.as_view(), name='gpu-details'),
            path('edit/', gpu_edit, name='gpu-edit'),
            path('delete/', gpu_delete, name='gpu-delete'),
        ]
    )),
    # path('list/', gpu_list, name='gpu-list'),
    path('list/', GpuListView.as_view(), name='gpu-list'),
]

from django.urls import path, include
from .views import cpu_create, cpu_edit, cpu_delete, CpuDetailView, CpuListView


urlpatterns = [
    path('create/', cpu_create, name='cpu-create'),
    path('<int:cpu_id>/', include(
        [
            # path('details/', cpu_details, name='cpu-details'),
            path('details/', CpuDetailView.as_view(), name='cpu-details'),
            path('edit/', cpu_edit, name='cpu-edit'),
            path('delete/', cpu_delete, name='cpu-delete'),
        ]
    )),
    # path('list/', cpu_list, name='cpu-list'),
    path('list/', CpuListView.as_view(), name='cpu-list'),
]

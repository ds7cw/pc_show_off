from django.urls import path, include
from .views import ram_create, ram_edit, ram_delete, RamDetailView, RamListView


urlpatterns = [
    path('create/', ram_create, name='ram-create'),
    path('<int:ram_id>/', include(
        [
            # path('details/', ram_details, name='ram-details'),
            path('details/', RamDetailView.as_view(), name='ram-details'),
            path('edit/', ram_edit, name='ram-edit'),
            path('delete/', ram_delete, name='ram-delete'),
        ]
    )),
    # path('list/', ram_list, name='ram-list'),
    path('list/', RamListView.as_view(), name='ram-list'),
]

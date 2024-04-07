from django.urls import path, include
from .views import storage_create, storage_edit, storage_details, storage_delete, storage_list


urlpatterns = [
    path('create/', storage_create, name='storage-create'),
    path('<int:storage_id>/', include(
        [
            path('details/', storage_details, name='storage-details'),
            path('edit/', storage_edit, name='storage-edit'),
            path('delete/', storage_delete, name='storage-delete'),
        ]
    )),
    path('list/', storage_list, name='storage-list'),
]
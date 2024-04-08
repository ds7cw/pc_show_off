from django.urls import path, include
from .views import pc_create, pc_edit, pc_details, pc_delete, pc_list, my_pc_list


urlpatterns = [
    path('create/', pc_create, name='pc-create'),
    path('<str:pc_name>/', include(
        [
            path('details/', pc_details, name='pc-details'),
            path('edit/', pc_edit, name='pc-edit'),
            path('delete/', pc_delete, name='pc-delete'),
        ]
    )),
    path('list/', pc_list, name='pc-list'),
    path('my-pc-list/', my_pc_list, name='my-pc-list'),
]
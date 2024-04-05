from django.urls import path, include
from .views import psu_create, psu_edit, psu_details, psu_delete, psu_list


urlpatterns = [
    path('create/', psu_create, name='psu-create'),
    path('<int:psu_id>/', include(
        [
            path('details/', psu_details, name='psu-details'),
            path('edit/', psu_edit, name='psu-edit'),
            path('delete/', psu_delete, name='psu-delete'),
        ]
    )),
    path('list/', psu_list, name='psu-list'),
]
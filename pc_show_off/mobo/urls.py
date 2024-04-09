from django.urls import path, include
from .views import mobo_create, mobo_edit, mobo_details, mobo_delete, mobo_list


urlpatterns = [
    path('create/', mobo_create, name='mobo-create'),
    path('<int:mobo_id>/', include(
        [
            path('details/', mobo_details, name='mobo-details'),
            path('edit/', mobo_edit, name='mobo-edit'),
            path('delete/', mobo_delete, name='mobo-delete'),
        ]
    )),
    path('list/', mobo_list, name='mobo-list'),
]
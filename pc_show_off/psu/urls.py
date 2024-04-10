from django.urls import path, include
from .views import psu_create, psu_edit, psu_delete, PsuDetailView, PsuListView


urlpatterns = [
    path('create/', psu_create, name='psu-create'),
    path('<int:psu_id>/', include(
        [
            # path('details/', psu_details, name='psu-details'),
            path('details/', PsuDetailView.as_view(), name='psu-details'),
            path('edit/', psu_edit, name='psu-edit'),
            path('delete/', psu_delete, name='psu-delete'),
        ]
    )),
    # path('list/', psu_list, name='psu-list'),
    path('list/', PsuListView.as_view(), name='psu-list'),
]

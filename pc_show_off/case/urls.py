from django.urls import path, include
from .views import case_create, case_edit, case_details, case_delete, case_list


urlpatterns = [
    path('create/', case_create, name='case-create'),
    path('<int:case_id>/', include(
        [
            path('details/', case_details, name='case-details'),
            path('edit/', case_edit, name='case-edit'),
            path('delete/', case_delete, name='case-delete'),
        ]
    )),
    path('list/', case_list, name='case-list'),
]
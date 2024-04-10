from django.urls import path, include
from .views import AppUserRegisterView, AppUserLoginView, AppUserLogoutView, details_page


urlpatterns = [
    path('register/', AppUserRegisterView.as_view(), name='register-page'),
    path('login/', AppUserLoginView.as_view(), name='login-page'),
    path('logout/', AppUserLogoutView.as_view(), name='logout-page'),
    path('details/<int:user_pk>/', details_page, name='profile-details'),
]
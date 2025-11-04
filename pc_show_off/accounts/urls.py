from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import AppUserRegisterView, AppUserLoginView, AppUserLogoutView, details_page


urlpatterns = [
    path('register/', AppUserRegisterView.as_view(), name='register-page'),
    path('login/', AppUserLoginView.as_view(), name='login-page'),
    path('logout/', AppUserLogoutView.as_view(), name='logout-page'),
    path('details/<int:user_pk>/', details_page, name='profile-details'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]
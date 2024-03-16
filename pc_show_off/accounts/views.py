from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model, views as auth_views

from .models import Profile
from .forms import AppUserCreationForm, AppUserChangeForm
# Create your views here.

UserModel = get_user_model()

class AppUserRegisterView(views.CreateView):

    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login-page')


class AppUserLoginView(auth_views.LoginView):

    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user) 
        
        return redirect(self.get_success_url())
    

class AppUserLogoutView(auth_views.LogoutView):

    pass

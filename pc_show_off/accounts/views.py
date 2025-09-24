import logging
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import AppUserCreationForm, AppUserChangeForm, ProfileChangeModelForm
# Create your views here.

UserModel = get_user_model()
logger = logging.getLogger(name=__name__)


class AppUserRegisterView(views.CreateView):

    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login-page')

    def form_valid(self, form):
        response = super().form_valid(form)
        logger.info("User with pk {} registered successfully". \
            format(self.object.pk))

        return response


class AppUserLoginView(auth_views.LoginView):

    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user) 
        logger.info("User with pk {} logged in successfully". \
            format(self.request.user.pk))

        return redirect(self.get_success_url())
    

class AppUserLogoutView(auth_views.LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logger.info("User with pk {} logged out successfully". \
                format(request.user.pk))
        return super().dispatch(request, *args, **kwargs)


login_required(login_url='login-page')
def details_page(request, user_pk):
    if user_pk != request.user.pk:
        return redirect('login-page')

    user_object = Profile.objects.select_related('user').filter(user__pk=user_pk).first()
    form = ProfileChangeModelForm(instance=user_object)
    context = {'form': form, 'profile': user_object}

    if request.method == 'POST':
        form = ProfileChangeModelForm(request.POST, instance=user_object)
        if form.is_valid():
            form.save()
            return redirect('profile-details', user_pk=user_object.pk)

    return render(request, 'accounts/profile-details.html', context)

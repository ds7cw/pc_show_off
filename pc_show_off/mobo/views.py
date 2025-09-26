import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, mixins as auth_mixins
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic as views
from django.urls import reverse, reverse_lazy

from .forms import CreateMoboModelForm, DeleteMoboModelForm
from .models import Mobo

logger = logging.getLogger(name=__name__)


# Create your views here.
@login_required(login_url='login-page')
def mobo_create(request):
    form = CreateMoboModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreateMoboModelForm()}
    logger.info(msg="User with pk {} opened a MoBo Creation Form".format(current_user.pk))

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                logger.info(msg="User with pk {} verified MoBo {} {}".format(
                    current_user.pk, new_instance.manufacturer, new_instance.model_name))
                current_user.profile.contributions += 1
                current_user.profile.save()
                logger.info(msg="Contributions of user with pk {} increased to {}".format(
                    current_user.pk, current_user.profile.contributions))

            new_instance.save()
            logger.info("User with pk {} created MoBo {} {}".format(
                current_user.pk, new_instance.manufacturer, new_instance.model_name))
            return redirect('mobo-list')

    return render(request, 'mobo/mobo-create.html', context)


@staff_member_required(login_url='login-page')
def mobo_edit(request, mobo_id):
    obj = Mobo.objects.select_related('contributor').get(pk=mobo_id)
    form = CreateMoboModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreateMoboModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_mobo = form.save(commit=False)

            if not updated_mobo.is_verified:
                updated_mobo.is_verified = True
                logger.info(msg="User with pk {} verified MoBo {} {}".format(
                    request.user.pk, updated_mobo.manufacturer, updated_mobo.model_name))
                obj.contributor.profiles.contributions += 1
                obj.contributor.profiles.save()
                logger.info(msg="Contributions of user with pk {} increased to {}".format(
                    obj.contributor.pk, obj.contributor.profile.contributions))

            updated_mobo.save()
            return redirect('mobo-list')

    return render(request, 'mobo/mobo-edit.html',context)


# @login_required(login_url='login-page')
# def mobo_details(request, mobo_id):
#     object = Mobo.objects.filter(pk=mobo_id).first()
#     context = {'object': object}

#     return render(request, 'mobo/mobo-details.html', context)


class MoboDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):

    model = Mobo
    template_name = 'mobo/mobo-details.html'
    context_object_name = 'object'
    login_url = reverse_lazy('login-page')

    def get_object(self, queryset=None):
        mobo_id = self.kwargs.get('mobo_id')
        return Mobo.objects.filter(pk=mobo_id).first()


@staff_member_required(login_url='login-page')
def mobo_delete(request, mobo_id):
    obj = Mobo.objects.filter(pk=mobo_id).first()
    form = DeleteMoboModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    logger.warning(msg="User with pk {} opened a MoBo Deletion Form for {} {}".format(
        request.user.pk, obj.manufacturer, obj.model_name))

    if request.method == 'POST':
        mobo_manufacturer = obj.manufacturer
        mobo_model_name = obj.model_name
        obj.delete()
        logger.warning(msg="MoBo {} {} deleted".format(
            mobo_manufacturer, mobo_model_name))
        return redirect('mobo-list')

    return render(request, 'mobo/mobo-delete.html', context)


# @login_required(login_url='login-page')
# def mobo_list(request):
#     all_objects = Mobo.objects.all().order_by('manufacturer', 'model_name')
#     verified_objects = all_objects.filter(is_verified=True)
#     not_verified_objects = all_objects.filter(is_verified=False)

#     context = {'verified': verified_objects, 'not_verified': not_verified_objects}

#     return render(request, 'mobo/mobo-list.html', context)


class MoboListView(auth_mixins.LoginRequiredMixin, views.ListView):

    model = Mobo
    template_name = 'mobo/mobo-list.html'
    login_url = reverse_lazy('login-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_objects = Mobo.objects.all().order_by('manufacturer', 'model_name')
        context['verified'] = all_objects.filter(is_verified=True)
        context['not_verified']  = all_objects.filter(is_verified=False)

        return context

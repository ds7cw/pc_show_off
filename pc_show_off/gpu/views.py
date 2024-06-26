from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, mixins as auth_mixins
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic as views
from django.urls import reverse, reverse_lazy

from .forms import CreateGpuModelForm, DeleteGpuModelForm
from .models import Gpu


# Create your views here.
@login_required(login_url='login-page')
def gpu_create(request):
    form = CreateGpuModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreateGpuModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                current_user.profile.contributions += 1
                current_user.profile.save()

            new_instance.save()
            return redirect('gpu-list')

    return render(request, 'gpu/gpu-create.html', context)


@staff_member_required(login_url='login-page')
def gpu_edit(request, gpu_id):
    obj = Gpu.objects.select_related('contributor').get(pk=gpu_id)
    form = CreateGpuModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreateGpuModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_gpu = form.save(commit=False)
            
            if not updated_gpu.is_verified:
                updated_gpu.is_verified = True
                obj.contributor.profiles.contributions += 1
                obj.contributor.profiles.save()
    
            updated_gpu.save()    
            return redirect('gpu-list')

    return render(request, 'gpu/gpu-edit.html',context)


# @login_required(login_url='login-page')
# def gpu_details(request, gpu_id):
#     object = Gpu.objects.filter(pk=gpu_id).first()
#     context = {'object': object}

#     return render(request, 'gpu/gpu-details.html', context)


class GpuDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):

    model = Gpu
    template_name = 'gpu/gpu-details.html'
    context_object_name = 'object'
    login_url = reverse_lazy('login-page')

    def get_object(self, queryset=None):
        gpu_id = self.kwargs.get('gpu_id')
        return Gpu.objects.filter(pk=gpu_id).first()


@staff_member_required(login_url='login-page')
def gpu_delete(request, gpu_id):
    object = Gpu.objects.filter(pk=gpu_id).first()
    form = DeleteGpuModelForm(instance=object)
    context = {'form': form, 'object': object}

    if request.method == 'POST':
        object.delete()
        return redirect('gpu-list')
    
    return render(request, 'gpu/gpu-delete.html', context)


# @login_required(login_url='login-page')
# def gpu_list(request):
#     all_objects = Gpu.objects.all().order_by('manufacturer', 'gpu_manufacturer','short_model_name')
#     verified_objects = all_objects.filter(is_verified=True)
#     not_verified_objects = all_objects.filter(is_verified=False)
    
#     context = {'verified': verified_objects, 'not_verified': not_verified_objects}

#     return render(request, 'gpu/gpu-list.html', context)


class GpuListView(auth_mixins.LoginRequiredMixin, views.ListView):

    model = Gpu
    template_name = 'gpu/gpu-list.html'
    login_url = reverse_lazy('login-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_objects = Gpu.objects.all().order_by('manufacturer', 'gpu_manufacturer','short_model_name')
        context['verified'] = all_objects.filter(is_verified=True)
        context['not_verified']  = all_objects.filter(is_verified=False)

        return context

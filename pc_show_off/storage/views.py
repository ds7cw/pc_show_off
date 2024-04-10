from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, mixins as auth_mixins
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic as views
from django.urls import reverse, reverse_lazy

from .forms import CreateStorageModelForm, DeleteStorageModelForm
from .models import Storage


# Create your views here.
@login_required(login_url='login-page')
def storage_create(request):
    form = CreateStorageModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreateStorageModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                current_user.profile.contributions += 1
                current_user.profile.save()

            new_instance.save()
            return redirect('storage-list')

    return render(request, 'storage/storage-create.html', context)


@staff_member_required(login_url='login-page')
def storage_edit(request, storage_id):
    obj = Storage.objects.select_related('contributor').get(pk=storage_id)
    form = CreateStorageModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreateStorageModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_storage = form.save(commit=False)
            
            if not updated_storage.is_verified:
                updated_storage.is_verified = True
                obj.contributor.profiles.contributions += 1
                obj.contributor.profiles.save()
    
            updated_storage.save()        
            return redirect('storage-list')

    return render(request, 'storage/storage-edit.html',context)


# @login_required(login_url='login-page')
# def storage_details(request, storage_id):
#     object = Storage.objects.filter(pk=storage_id).first()
#     context = {'object': object}

#     return render(request, 'storage/storage-details.html', context)


class StorageDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):

    model = Storage
    template_name = 'storage/storage-details.html'
    context_object_name = 'object'
    login_url = reverse_lazy('login-page')

    def get_object(self, queryset=None):
        storage_id = self.kwargs.get('storage_id')
        return Storage.objects.filter(pk=storage_id).first()


@staff_member_required(login_url='login-page')
def storage_delete(request, storage_id):
    object = Storage.objects.filter(pk=storage_id).first()
    form = DeleteStorageModelForm(instance=object)
    context = {'form': form, 'object': object}

    if request.method == 'POST':
        object.delete()
        return redirect('storage-list')
    
    return render(request, 'storage/storage-delete.html', context)


# @login_required(login_url='login-page')
# def storage_list(request):
#     all_objects = Storage.objects.all().order_by('total_storage', 'manufacturer', 'series')
#     verified_objects = all_objects.filter(is_verified=True)
#     not_verified_objects = all_objects.filter(is_verified=False)
    
#     context = {'verified': verified_objects, 'not_verified': not_verified_objects}

#     return render(request, 'storage/storage-list.html', context)


class StorageListView(auth_mixins.LoginRequiredMixin, views.ListView):

    model = Storage
    template_name = 'storage/storage-list.html'
    login_url = reverse_lazy('login-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_objects = Storage.objects.all().order_by('total_storage', 'manufacturer', 'series')
        context['verified'] = all_objects.filter(is_verified=True)
        context['not_verified']  = all_objects.filter(is_verified=False)

        return context

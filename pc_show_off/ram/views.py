from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

from .forms import CreateRamModelForm, DeleteRamModelForm
from .models import Ram


# Create your views here.
@login_required(login_url='login-page')
def ram_create(request):
    form = CreateRamModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreateRamModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                current_user.profile.contributions += 1
                current_user.profile.save()

            new_instance.save()
            return redirect('ram-list')

    return render(request, 'ram/ram-create.html', context)


@staff_member_required(login_url='login-page')
def ram_edit(request, ram_id):
    obj = Ram.objects.select_related('contributor').get(pk=ram_id)
    form = CreateRamModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreateRamModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_ram = form.save(commit=False)
            updated_ram.is_verified = True
            updated_ram.save()
            
            obj.contributor.profile.contributions += 1
            obj.contributor.profile.save()
            return redirect('ram-list')

    return render(request, 'ram/ram-edit.html',context)


@login_required(login_url='login-page')
def ram_details(request, ram_id):
    object = Ram.objects.filter(pk=ram_id).first()
    context = {'object': object}

    return render(request, 'ram/ram-details.html', context)


@staff_member_required(login_url='login-page')
def ram_delete(request, ram_id):
    object = Ram.objects.filter(pk=ram_id).first()
    form = DeleteRamModelForm(instance=object)
    context = {'form': form, 'object': object}

    if request.method == 'POST':
        object.delete()
        return redirect('ram-list')
    
    return render(request, 'ram/ram-delete.html', context)


@login_required(login_url='login-page')
def ram_list(request):
    all_objects = Ram.objects.all().order_by('memory_type', 'max_frequency', 'manufacturer', 'series')
    verified_objects = all_objects.filter(is_verified=True)
    not_verified_objects = all_objects.filter(is_verified=False)
    
    context = {'verified': verified_objects, 'not_verified': not_verified_objects}

    return render(request, 'ram/ram-list.html', context)

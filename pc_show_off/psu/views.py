from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

from .forms import CreatePsuModelForm, DeletePsuModelForm
from .models import Psu


# Create your views here.
@login_required(login_url='login-page')
def psu_create(request):
    form = CreatePsuModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreatePsuModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                current_user.profile.contributions += 1
                current_user.profile.save()

            new_instance.save()
            return redirect('psu-list')

    return render(request, 'psu/psu-create.html', context)


@staff_member_required(login_url='login-page')
def psu_edit(request, psu_id):
    obj = Psu.objects.select_related('contributor').get(pk=psu_id)
    form = CreatePsuModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreatePsuModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_psu = form.save(commit=False)
            updated_psu.is_verified = True
            updated_psu.save()
            
            obj.contributor.profile.contributions += 1
            obj.contributor.profile.save()
            return redirect('psu-list')

    return render(request, 'psu/psu-edit.html',context)


@login_required(login_url='login-page')
def psu_details(request, psu_id):
    object = Psu.objects.filter(pk=psu_id).first()
    context = {'object': object}

    return render(request, 'psu/psu-details.html', context)


@staff_member_required(login_url='login-page')
def psu_delete(request, psu_id):
    object = Psu.objects.filter(pk=psu_id).first()
    form = DeletePsuModelForm(instance=object)
    context = {'form': form, 'object': object}

    if request.method == 'POST':
        object.delete()
        return redirect('psu-list')
    
    return render(request, 'psu/psu-delete.html', context)


@login_required(login_url='login-page')
def psu_list(request):
    all_objects = Psu.objects.all().order_by('manufacturer', 'model_name')
    verified_objects = all_objects.filter(is_verified=True)
    not_verified_objects = all_objects.filter(is_verified=False)
    
    context = {'verified': verified_objects, 'not_verified': not_verified_objects}

    return render(request, 'psu/psu-list.html', context)

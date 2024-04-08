from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

from .forms import CreatePcModelForm, DeletePcModelForm
from .models import Pc


# Create your views here.
def get_pc_and_select_related(): # Should result in less Queries
    my_pc = Pc.objects.select_related(
        'owner',
        'cpu_part',
        'gpu_part',
        'mobo_part',
        'ram_part',
        'psu_part',
        'storage_part',
        'case_part',
    )

    return my_pc


@login_required(login_url='login-page')
def pc_create(request):
    form = CreatePcModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreatePcModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.owner = current_user
            new_instance.save()
            return redirect('my-pc-list')

    return render(request, 'pc/pc-create.html', context)


login_required(login_url='login-page')
def my_pc_list(request):
    all_pcs = get_pc_and_select_related()
    user_pcs = all_pcs.filter(owner__pk=request.user.pk)
    context = {'objects': user_pcs}

    return render(request, 'pc/my-pc-list.html', context)



@staff_member_required(login_url='login-page')
def pc_edit(request, pc_name):
    all_pcs = get_pc_and_select_related()
    obj = all_pcs.filter(owner__pk=request.user.pk, pc_name=pc_name).first()
    form = CreatePcModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreatePcModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_pc = form.save(commit=False)
            updated_pc.is_verified = True
            updated_pc.save()
            
            return redirect('my-pc-list')

    return render(request, 'pc/pc-edit.html',context)



@login_required(login_url='login-page')
def pc_details(request, pc_name):
    all_pcs = get_pc_and_select_related()
    object = all_pcs.filter(pc_name=pc_name).first()
    context = {'object': object}

    return render(request, 'pc/pc-details.html', context)


@login_required(login_url='login-page')
def pc_delete(request, pc_name):
    all_pcs = get_pc_and_select_related()
    object = all_pcs.filter(owner__pk=request.user.pk, pc_name=pc_name).first()
    form = DeletePcModelForm(instance=object)
    context = {'form': form, 'object': object}

    if request.method == 'POST':
        object.delete()
        return redirect('my-pc-list')
    
    return render(request, 'pc/pc-delete.html', context)


@login_required(login_url='login-page')
def pc_list(request):
    all_objects = get_pc_and_select_related()    
    context = {'objects': all_objects}

    return render(request, 'pc/pc-list.html', context)

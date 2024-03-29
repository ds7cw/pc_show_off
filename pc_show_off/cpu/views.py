from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

from .forms import CreateCpuModelForm
from .models import Cpu


# Create your views here.
@login_required(login_url='login-page')
def cpu_create(request):
    form = CreateCpuModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreateCpuModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                current_user.profile.contributions += 1
                current_user.profile.save()

            new_instance.save()
            return redirect('index-page')

    return render(request, 'cpu/cpu-create.html', context)


@staff_member_required(login_url='login-page')
def cpu_edit(request, cpu_id):
    cpu_obj = Cpu.objects.select_related('contributor').get(pk=cpu_id)
    form = CreateCpuModelForm(instance=cpu_obj)
    context = {'form': form, 'cpu': cpu_obj}
    print(cpu_obj.contributor.profile.contributions)

    if request.method == 'POST':
        form = CreateCpuModelForm(request.POST, instance=cpu_obj)

        if form.is_valid():
            updated_cpu = form.save(commit=False)
            updated_cpu.is_verified = True
            updated_cpu.save()
            
            cpu_obj.contributor.profile.contributions += 1
            cpu_obj.contributor.profile.save()
            return redirect()

    return render(request, 'cpu/cpu-edit.html',context)


def cpu_details(request, cpu_id):
    pass


def cpu_delete(request, cpu_id):
    pass


@login_required(login_url='login-page')
def cpu_list(request):
    verified_cpus = Cpu.objects.filter(is_verified=True)
    not_verified_cpus = Cpu.objects.filter(is_verified=False)
    
    context = {'verified': verified_cpus, 'not_verified': not_verified_cpus}

    return render(request, 'cpu/cpu-list.html', context)

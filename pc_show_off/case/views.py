from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, mixins as auth_mixins
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic as views
from django.urls import reverse, reverse_lazy

from .forms import CreateCaseModelForm, DeleteCaseModelForm
from .models import Case


# Create your views here.
@login_required(login_url='login-page')
def case_create(request):
    form = CreateCaseModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreateCaseModelForm()}

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.contributor = current_user

            if current_user.is_staff: # If created by staff member, assume naming conventions are correct
                new_instance.is_verified = True
                current_user.profile.contributions += 1
                current_user.profile.save()

            new_instance.save()
            return redirect('case-list')

    return render(request, 'case/case-create.html', context)


@staff_member_required(login_url='login-page')
def case_edit(request, case_id):
    obj = Case.objects.select_related('contributor').get(pk=case_id)
    form = CreateCaseModelForm(instance=obj)
    context = {'form': form, 'object': obj}

    if request.method == 'POST':
        form = CreateCaseModelForm(request.POST, instance=obj)

        if form.is_valid():
            updated_case = form.save(commit=False)
            
            if not updated_case.is_verified:
                updated_case.is_verified = True        
                obj.contributor.profiles.contributions += 1
                obj.contributor.profiles.save()
    
            updated_case.save()
            return redirect('case-list')

    return render(request, 'case/case-edit.html',context)


# @login_required(login_url='login-page')
# def case_details(request, case_id):
#     object = Case.objects.filter(pk=case_id).first()
#     context = {'object': object}

#     return render(request, 'case/case-details.html', context)


class CaseDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):

    model = Case
    template_name = 'case/case-details.html'
    context_object_name = 'object'
    login_url = reverse_lazy('login-page')

    def get_object(self, queryset=None):
        case_id = self.kwargs.get('case_id')
        return Case.objects.filter(pk=case_id).first()


@staff_member_required(login_url='login-page')
def case_delete(request, case_id):
    object = Case.objects.filter(pk=case_id).first()
    form = DeleteCaseModelForm(instance=object)
    context = {'form': form, 'object': object}

    if request.method == 'POST':
        object.delete()
        return redirect('case-list')
    
    return render(request, 'case/case-delete.html', context)


# @login_required(login_url='login-page')
# def case_list(request):
#     all_objects = Case.objects.all().order_by('manufacturer', 'series', 'model_name')
#     verified_objects = all_objects.filter(is_verified=True)
#     not_verified_objects = all_objects.filter(is_verified=False)
    
#     context = {'verified': verified_objects, 'not_verified': not_verified_objects}

#     return render(request, 'case/case-list.html', context)


class CaseListView(auth_mixins.LoginRequiredMixin, views.ListView):

    model = Case
    template_name = 'case/case-list.html'
    login_url = reverse_lazy('login-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_objects = Case.objects.all().order_by('manufacturer', 'series', 'model_name')
        context['verified'] = all_objects.filter(is_verified=True)
        context['not_verified']  = all_objects.filter(is_verified=False)

        return context

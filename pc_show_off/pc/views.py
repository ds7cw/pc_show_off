import logging
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

from .forms import CreatePcModelForm, DeletePcModelForm, PcRatingModelForm, PcCommentModelForm
from .models import Pc, PcRating, PcComment

logger = logging.getLogger(__name__)


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
    ).prefetch_related('ratings', 'comments')

    return my_pc


@login_required(login_url='login-page')
def pc_create(request):
    form = CreatePcModelForm(request.POST or None)
    UserModel = get_user_model()
    current_user = UserModel.objects.get(pk=request.user.pk)
    context = {'form': CreatePcModelForm()}
    logger.info(msg="User with pk {} opened a PC Creation Form".format(current_user.pk))

    if request.method == 'POST':
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.owner = current_user
            new_instance.save()
            logger.info("User with pk {} created PC {} w/ {} & {}".format(current_user.pk,
                new_instance.pc_name, new_instance.cpu_part, new_instance.gpu_part))
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
            logger.info("User with pk {} updated PC {} w/ {} & {}".format(request.user.pk,
                updated_pc.pc_name, updated_pc.cpu_part, updated_pc.gpu_part))

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
    obj = all_pcs.filter(owner__pk=request.user.pk, pc_name=pc_name).first()
    form = DeletePcModelForm(instance=obj)
    context = {'form': form, 'object': obj}
    user_id = request.user.pk

    logger.warning(msg="User with pk {} opened a PC Deletion Form for {} [{}, {}, {}]".format(
        user_id, obj.pc_name, obj.cpu_part.model_name, obj.gpu_part.short_model_name, obj.mobo_part.model_name))

    if request.method == 'POST':
        pc_name = obj.pc_name
        cpu_part = obj.cpu_part.model_name
        gpu_part = obj.gpu_part.short_model_name
        mobo_part = obj.mobo_part.model_name
        obj.delete()
        logger.warning(msg="PC {} [{}, {}, {}] deleted".format(
            pc_name, cpu_part, gpu_part, mobo_part))
        return redirect('my-pc-list')

    return render(request, 'pc/pc-delete.html', context)


@login_required(login_url='login-page')
def pc_list(request):
    all_objects = get_pc_and_select_related()
    all_objects = all_objects.annotate(rating=Avg('ratings__rating_value'))
    context = {'objects': all_objects}

    return render(request, 'pc/pc-list.html', context)


@login_required(login_url='login-page')
def pc_rating(request, pc_name):
    all_objects = get_pc_and_select_related()
    current_pc = all_objects.filter(pc_name=pc_name).first()

    if not current_pc:
        return redirect('pc-list')

    if request.method == 'POST':
        form = PcRatingModelForm(request.POST)
        if form.is_valid:
            current_user = get_user_model()
            current_user = current_user.objects.get(pk=request.user.pk)
            existing_rating = PcRating.objects.filter(reviewer=current_user, pc=current_pc).first()
            if existing_rating:
                form = PcRatingModelForm(request.POST, instance=existing_rating)
                form.save()
            else:
                new_rating = form.save(commit=False)
                new_rating.reviewer = current_user
                new_rating.pc = current_pc
                new_rating.save()
            return redirect('pc-list')

    form = PcRatingModelForm()
    context = {'form': form, 'object': current_pc}

    return render(request, 'pc/pc-rating.html', context)


login_required(login_url='login-page')
def pc_comment(request, pc_name):
    all_objects = get_pc_and_select_related()
    current_pc = all_objects.filter(pc_name=pc_name).first()
    current_user = get_user_model()
    current_user = current_user.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        form = PcCommentModelForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pc = current_pc
            new_comment.author = current_user
            new_comment.save()
            return redirect('pc-list')

    form = PcCommentModelForm()
    context = {'form': form, 'object': current_pc}

    return render(request, 'pc/pc-comment.html', context)

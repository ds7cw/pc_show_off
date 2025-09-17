from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    context = {}

    return render(request, 'common/index-page.html', context)


def components_library(request):
    context = {}

    return render(request, 'common/components-library.html', context)


def contributors(request):
    all_users = get_user_model()
    all_users = all_users.objects.prefetch_related('profile').order_by('-profile__contributions')
    context = {'objects': all_users}

    return render(request, 'common/contributors.html', context)
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}

    return render(request, 'common/index-page.html', context)


def components_library(request):
    context = {}

    return render(request, 'common/components-library.html', context)
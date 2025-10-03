from rest_framework import viewsets
from .models import Gpu
from .serializers import GpuSerializer


class GpuViewSet(viewsets.ModelViewSet):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer

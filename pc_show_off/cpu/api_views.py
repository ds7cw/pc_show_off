from rest_framework import viewsets
from .models import Cpu
from .serializers import CpuSerializer


class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

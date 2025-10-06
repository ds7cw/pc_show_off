from rest_framework import viewsets
from .models import Ram
from .serializers import RamSerializer


class RamViewSet(viewsets.ModelViewSet):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer

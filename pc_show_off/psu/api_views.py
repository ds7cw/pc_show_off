from rest_framework import viewsets
from .models import Psu
from .serializers import PsuSerializer


class PsuViewSet(viewsets.ModelViewSet):
    queryset = Psu.objects.all()
    serializer_class = PsuSerializer

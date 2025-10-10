from rest_framework import viewsets
from .models import Pc
from .serializers import PcSerializer


class PcViewSet(viewsets.ModelViewSet):
    queryset = Pc.objects.all()
    serializer_class = PcSerializer

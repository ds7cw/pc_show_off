from rest_framework import viewsets
from .models import Mobo
from .serializers import MoboSerializer


class MoboViewSet(viewsets.ModelViewSet):
    queryset = Mobo.objects.all()
    serializer_class = MoboSerializer

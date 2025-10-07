from rest_framework import viewsets
from .models import Storage
from .serializers import StorageSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

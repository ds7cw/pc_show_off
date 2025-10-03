from rest_framework import serializers
from .models import Gpu


class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'

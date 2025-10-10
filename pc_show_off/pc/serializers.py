from rest_framework import serializers
from .models import Pc


class PcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pc
        fields = '__all__'

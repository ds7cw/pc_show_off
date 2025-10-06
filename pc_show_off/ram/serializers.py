from rest_framework import serializers
from .models import Ram


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'

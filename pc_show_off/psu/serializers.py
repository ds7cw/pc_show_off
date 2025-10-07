from rest_framework import serializers
from .models import Psu


class PsuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psu
        fields = '__all__'

from rest_framework import serializers
from .models import Mobo


class MoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobo
        fields = '__all__'

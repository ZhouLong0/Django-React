from rest_framework import serializers
from .models import ModelClass

class ModelClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelClass
        fields = ('id', 'code', 'host', ...)

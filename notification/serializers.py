from rest_framework import serializers
from .models import UserSupport


class SupportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserSupport
        fields = ["massage"]
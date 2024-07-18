from rest_framework import serializers
from .models import VisaApplication


class VisaApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaApplication
        fields = '__all__'
        read_only_fields = ['user']



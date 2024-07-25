from rest_framework import serializers
from .models import VisaApplication, VisaStatus


class VisaApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaApplication
        fields = '__all__'
        read_only_fields = ['user']


class VisaStatusSerializer(serializers.ModelField):
    class Meta:
        model = VisaStatus
        fields = '__all__'

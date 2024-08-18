from rest_framework import serializers
from .models import VisaApplication, VisaStatus

class VisaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaStatus
        fields = '__all__'


class VisaApplicationSerializer(serializers.ModelSerializer):
    visa_statuses = VisaStatusSerializer(many=True, read_only=True)
    class Meta:
        model = VisaApplication
        fields = '__all__'
        read_only_fields = ['user']

 

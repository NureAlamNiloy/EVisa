from rest_framework import serializers
from .models import VisaApplication, VisaStatus
import base64

class VisaStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VisaStatus
        fields ='__all__'

class VisaApplicationSerializer(serializers.ModelSerializer):
    visa_statuses = VisaStatusSerializer(many=True, read_only=True)
    encoded_id = serializers.SerializerMethodField()
    class Meta:
        model = VisaApplication
        fields = '__all__'
        read_only_fields = ['user']
    
    def get_encoded_id(self, obj):
        encoded_id = base64.urlsafe_b64encode(str(obj.id).encode())
        return encoded_id

 

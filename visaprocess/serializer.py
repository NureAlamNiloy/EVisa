from rest_framework import serializers
from .models import VisaApplication


class VisaApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaApplication
        fields = ["visa_type", "passport_no"]



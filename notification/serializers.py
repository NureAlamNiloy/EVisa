from rest_framework import serializers
from .models import notification


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = notification
        fields = ["title","massage", "created_at"]
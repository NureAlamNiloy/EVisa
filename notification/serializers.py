from rest_framework import serializers
from .models import notification


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = notification
        fields = ["title","message", "created_at"]
        read_only_fields = ['user']
    
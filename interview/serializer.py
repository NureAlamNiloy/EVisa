from rest_framework import serializers
from .models import InterviewDate, InterviewBooking


class InterviewDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewDate
        fields = ['id', 'interview_date']


class InterviewBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewBooking
        fields = '__all__'
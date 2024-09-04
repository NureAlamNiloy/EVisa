from rest_framework import serializers
from .models import Appointment, NoInterview, ScheduleSlot


class NoInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoInterview
        fields = '__all__'


class ScheduleSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSlot
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["visa_application","interview_date","booked_at"]

    def validate(self, data):
        date = data.get('interview_date')
        if Appointment.objects.filter(interview_date=date).count() >=2:
            raise serializers.ValidationError("No more appointments available on this date.")
        
        visa_application = data.get('visa_application')
        if Appointment.objects.filter(visa_application=visa_application).exists():
            raise serializers.ValidationError("You have already booked an appointment for this visa application.")
        
        return data
from rest_framework import serializers
from .models import Appointment, AdminInterviewInfo, ScheduleSlot


class AdminInterviewInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInterviewInfo
        fields = '__all__'


class ScheduleSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSlot
        fields =  '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['visa_application', 'user', 'schedule_slot', 'booked_at']
        read_only_fields = ['booked_at']

    def validate(self, data):
        # Custom validation logic if needed
        schedule_slot = data.get('schedule_slot')
        if schedule_slot.is_booked:
            raise serializers.ValidationError("This slot is already booked.")
        return data
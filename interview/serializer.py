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
    # aikhane sourse use kore onno ekta model er data ai api er moddhe niye asa hoisee
    interview_date = serializers.DateField(source='schedule_slot.interview_date', read_only=True)
    start_time = serializers.TimeField(source='schedule_slot.start_time', read_only=True)
    slot_duration = serializers.TimeField(source='schedule_slot.slot_duration', read_only=True)
    

    class Meta:
        model = Appointment
        fields = '__all__'
        # read_only_fields = ['visa_application', 'schedule_slot', 'interview_date', 'start_time']

    def validate(self, data):
        schedule_slot = data.get('schedule_slot')
        if schedule_slot is None:
            raise serializers.ValidationError("Schedule slot must be provided.")
        schedule_slot_instance = ScheduleSlot.objects.get(pk=schedule_slot.id)
        
        if schedule_slot_instance.is_booked:
            raise serializers.ValidationError("This slot is already booked.")
        
        return data
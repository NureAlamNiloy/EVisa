from rest_framework import serializers
from .models import VisaApplication, VisaStatus
from interview.serializer import AppointmentSerializer, ScheduleSlotSerializer
from interview.models import Appointment, ScheduleSlot
import base64

class VisaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaStatus
        fields ='__all__'

class VisaApplicationSerializer(serializers.ModelSerializer):
    
    visa_statuses = VisaStatusSerializer(many=True, read_only=True)
    encoded_id = serializers.SerializerMethodField()
    # Appointment module ee visaApplication er relation ee related name appointment set kora ase tai ei filed diye serializer diye application er moddhe specific appointment dekhano jaitasee
    interview_date = serializers.SerializerMethodField()
    interview_start_time = serializers.SerializerMethodField()
    
    class Meta:
        model = VisaApplication
        fields = '__all__'
        read_only_fields = ['user']
        

    def get_encoded_id(self, obj):
        encoded_id = base64.urlsafe_b64encode(str(obj.id).encode())
        return encoded_id
   
    def get_interview_date(self, obj):
        appointment = Appointment.objects.filter(visa_application=obj).first()
        if appointment and appointment.schedule_slot:
            return appointment.schedule_slot.interview_date
        return None

    def get_interview_start_time(self, obj):
        appointment = Appointment.objects.filter(visa_application=obj).first()
        if appointment and appointment.schedule_slot:
            return appointment.schedule_slot.start_time
        return None





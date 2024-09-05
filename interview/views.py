from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from .models import Appointment, AdminInterviewInfo, ScheduleSlot
from .serializer import AppointmentSerializer, AdminInterviewInfoSerializer, ScheduleSlotSerializer
from datetime import datetime, timedelta, time


# Create your views here.


def generate_interview_slots_for_year():
    pass

class AdminInterviewInfoViewset(APIView):
    pass 

class ScheduleSlotViewset(APIView):
    pass       

class AppointmentViewset(APIView):
    pass 





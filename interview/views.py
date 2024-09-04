from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Count
from .models import Appointment, NoInterview, ScheduleSlot
from .serializer import AppointmentSerializer, NoInterviewSerializer, ScheduleSlotSerializer
from rest_framework.permissions import IsAuthenticated 



# Create your views here.

class NoInterviewViewset(APIView):
    pass


class ScheduleSlotViewset(APIView):
    pass


class AppointmentViewset(APIView):
    pass



from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializer import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



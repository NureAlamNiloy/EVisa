from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import VisaApplication
from .serializer import VisaApplicationSerializer

# Create your views here.

class VisaApplicationViewset(viewsets.ModelViewSet):
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

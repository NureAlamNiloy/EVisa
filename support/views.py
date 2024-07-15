from django.shortcuts import render
from rest_framework import viewsets
from .models import UserSupport
from .serializer import SupportSerializer

# Create your views here.

class SupportViewset(viewsets.ModelViewSet):
    queryset = UserSupport.objects.all()
    serializer_class = SupportSerializer



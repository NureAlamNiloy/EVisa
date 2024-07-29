from django.shortcuts import render
from rest_framework import views, viewsets
from .models import notification
from .serializers import NotificationSerializer

# Create your views here.

class NotificationView(viewsets.ModelViewSet):
    queryset = notification.objects.all()
    serializer_class = NotificationSerializer



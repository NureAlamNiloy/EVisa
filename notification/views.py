from django.shortcuts import render
from rest_framework import views, viewsets
from .models import notification
from .serializer import NotificationSerializer

# Create your views here.

class NotificationView(viewsets.ModelViewSet):
    queryset = notification.objects.all()
    serializer_class = NotificationSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)




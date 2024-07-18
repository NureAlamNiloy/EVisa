from django.shortcuts import render
from rest_framework import viewsets
from .models import UserSupport
from .serializer import SupportSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SupportViewset(viewsets.ModelViewSet):
    queryset = UserSupport.objects.all()
    serializer_class = SupportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



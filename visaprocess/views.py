from django.shortcuts import render
from rest_framework import viewsets, permissions, views
from .models import VisaApplication, VisaStatus
from .serializer import VisaApplicationSerializer, VisaStatusSerializer
from rest_framework.response import Response  

# Create your views here.

class VisaApplicationViewset(viewsets.ModelViewSet):
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class VisaStatusViewset(views.APIView):
    queryset = VisaStatus.objects.all()
    serializer_class = VisaStatusSerializer

    # def get(self,request, tracking_id, format=None):
    #     try:

    #     except VisaStatus.DoesNotExist:
    #         return Response{"massage:"}

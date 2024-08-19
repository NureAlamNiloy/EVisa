from django.shortcuts import render
from rest_framework import viewsets, views, exceptions
from .models import VisaApplication, VisaStatus
from .serializer import VisaApplicationSerializer, VisaStatusSerializer
from rest_framework.response import Response  
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
 
class VisaApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer
    
    def retrieve(self, request, *args, **kwargs):
        # This handles GET for a specific application and includes the status
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class VisaStatusViewset(views.APIView):
    queryset = VisaStatus.objects.all()
    serializer_class = VisaStatusSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request, tracking_id, format=None):
        try:
            visa_status = VisaStatus.objects.get(tracking_id=tracking_id)
            serializer = VisaStatusSerializer(visa_status)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except VisaStatus.DoesNotExist:
            return Response({"message: Traking id not found"}, status = status.HTTP_404_NOT_FOUND)
    
    def patch(self,request, tracking_id, *args, **kwargs):
        try:
            visa_status = VisaStatus.objects.get(tracking_id=tracking_id)
            serializer = VisaStatusSerializer(visa_status, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except VisaStatus.DoesNotExist:
            return Response({"message": "Tracking ID not found"}, status=status.HTTP_404_NOT_FOUND)


class CountTotalUserApplication(views.APIView):
    def get(self, request, user_id):
        if request.user.id != int(user_id):
            return Response({"message": "You do not have permission to view this user's data."}, status=status.HTTP_403_FORBIDDEN)
        
        total_application = VisaApplication.objects.filter(user_id=user_id).count()
        return Response({"user_id": user_id, "application_Count": total_application}, status=status.HTTP_200_OK)



from django.shortcuts import render
from rest_framework import viewsets, views, exceptions
from .models import VisaApplication, VisaStatus
from .serializer import VisaApplicationSerializer, VisaStatusSerializer
from rest_framework.response import Response  
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from account.authentication import CsrfExemptSessionAuthentication


# Create your views here.
 
class VisaApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CsrfExemptSessionAuthentication]
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer
    

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        # print(f'This my token {self.request.user.token}')

class VisaStatusViewset(views.APIView):
    queryset = VisaStatus.objects.all()
    serializer_class = VisaStatusSerializer

    def get(self,request, tracking_id, format=None):
        try:
            visa_status = VisaStatus.objects.get(traking_id=tracking_id)
            serializer = VisaStatusSerializer(visa_status)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except VisaStatus.DoesNotExist:
            return Response({"message: Traking id not found"}, status = status.HTTP_404_NOT_FOUND)

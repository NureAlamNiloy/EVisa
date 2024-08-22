from rest_framework import viewsets, views, filters, pagination
from .models import VisaApplication, VisaStatus
from .serializer import VisaApplicationSerializer, VisaStatusSerializer
from rest_framework.response import Response  
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64


# Create your views here.

class ListPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 200
 
class VisaApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer
    pagination_class = ListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email', 'phone_number']
    
    def retrieve(self, request, *args, **kwargs):
        try:
            decoded_bytes = base64.urlsafe_b64decode(kwargs['pk']) 
            decoded_id = int(decoded_bytes.decode('utf-8'))
            instance = self.get_queryset().get(id=decoded_id)
            serializer = self.get_serializer(instance)
            print(decoded_bytes)
            print(decoded_id)
        except ValueError:
             return Response({"message: Id not found"}, status = status.HTTP_404_NOT_FOUND) 
        
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
                return Response({"message": "Status Update Successfully Hridoy Pagla"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except VisaStatus.DoesNotExist:
            return Response({"message": "Tracking ID not found"}, status=status.HTTP_404_NOT_FOUND)


class UserAllApplication(views.APIView):
    pagination_class = ListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email', 'phone_number', 'user__username']
    def get(self, request, user_id):
        if request.user.id != int(user_id):
            return Response({"message": "You do not have permission to view this user's data."}, status=status.HTTP_403_FORBIDDEN)
        
        total_application = VisaApplication.objects.filter(user_id=user_id)
        serializer = VisaApplicationSerializer(total_application, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



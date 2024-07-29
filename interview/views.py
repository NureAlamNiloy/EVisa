from django.shortcuts import render
from rest_framework import views, viewsets, status
from rest_framework.response import Response 
from .serializer import InterviewBookingSerializer, InterviewDateSerializer
from .models import InterviewBooking, InterviewDate
from visaprocess.models import VisaStatus

# Create your views here.

class InterviewDateView(views.APIView):
    def get(self, request, format=None):
        available_date = [date for date in InterviewDate.objects.all() if date.is_available()]
        serializer = InterviewDateSerializer(available_date, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterviewBookingView(views.APIView):
    def post(self, request, format=None):
        date_id = request.data.get('date_id')
        application_id = request.data.get('application_id')
        try:
            slot = InterviewDate.objects.get(id=date_id)
            visa_status = VisaStatus.objects.get(visa_id=application_id, visa_status='Approved')
            if not slot.is_available():
                return Response({"massage":"Date is not available"}, status=status.HTTP_400_BAD_REQUEST)
            
            booking = InterviewBooking(user=request.user, slot=slot, visa_application=visa_status.visa)
            booking.save()
            return Response({"message": "Interview slot booked successfully."}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        




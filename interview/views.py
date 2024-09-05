from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from .models import Appointment, NoInterview, ScheduleSlot
from .serializer import AppointmentSerializer, NoInterviewSerializer, ScheduleSlotSerializer
from datetime import datetime, timedelta, time


# Create your views here.



class NoInterviewViewset(APIView):
    def post(self, request):
        serializer = NoInterviewSerializer(data=request.data, many=True)
        if serializer.is_valid():
            no_interview_dates = [item['no_interview_date'] for item in serializer.validated_data]
        
            for date in no_interview_dates:
                NoInterview.objects.get_or_create(no_interview_date=date)
            ScheduleSlot.objects.filter(interview_date__in=no_interview_dates).delete()

            return Response({'message': 'No-interview dates updated successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        no_interview_dates = NoInterview.objects.all()
        serializer = NoInterviewSerializer(no_interview_dates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ScheduleSlotViewset(APIView):
    pass


class AppointmentViewset(APIView):
    pass



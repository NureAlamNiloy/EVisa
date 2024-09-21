from rest_framework.response import Response
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .models import Appointment, AdminInterviewInfo, ScheduleSlot
from .serializer import AppointmentSerializer, AdminInterviewInfoSerializer, ScheduleSlotSerializer
from datetime import datetime, timedelta
from django.db.models import Count,Q,F
from visaprocess.serializer import VisaApplicationSerializer
from visaprocess.models import VisaApplication
from django.shortcuts import get_object_or_404


class GetStartEndDate(APIView):
    def get(self, request):
        try:
            booked_dates = (
                ScheduleSlot.objects.values('interview_date')
                .annotate(total_slots=Count('id'), booked_slots=Count('id', filter=Q(is_booked=True)))
                .filter(total_slots=F('booked_slots'))
                .values_list('interview_date', flat=True)
            )
            interview_info = AdminInterviewInfo.objects.latest('id')
            serializer = AdminInterviewInfoSerializer(interview_info)
            return Response({
                "start_date": serializer.data['start_date'],
                "end_date": serializer.data['end_date'],
                "fully_booked_dates": list(booked_dates)
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminInterviewInfoViewset(APIView):
    
    def post(self, request):
        serializer = AdminInterviewInfoSerializer(data=request.data)
        if serializer.is_valid():
            interview_info = serializer.save()
            total_interview = request.data.get('total_interview', interview_info.total_interview)


            self.generate_interview_slots(interview_info.start_date, interview_info.end_date, interview_info.start_time, interview_info.end_time, total_interview)
            return Response({"message": f"Interview slots created successfully from {interview_info.start_date} to {interview_info.end_date}"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_interview_slots(self, start_date, end_date, start_time, end_time, total_interview):
        current_date = start_date
        while current_date <= end_date:
            
            if ScheduleSlot.objects.filter(interview_date=current_date).exists():
                current_date += timedelta(days=1)
                continue


            current_start_time = datetime.combine(current_date, start_time)
            current_end_time = datetime.combine(current_date, end_time)

            if current_start_time >= current_end_time:
                raise ValueError("Start time must be earlier than end time")


            total_available_time = current_end_time - current_start_time
            slot_duration = total_available_time / total_interview  


            for _ in range(total_interview):
                ScheduleSlot.objects.create(slot_duration=slot_duration, interview_date=current_date, start_time=current_start_time.time())
                current_start_time += slot_duration
                
            current_date += timedelta(days=1)




class ScheduleSlotViewset(APIView):
    def get(self, request):
        
        interview_date = request.query_params.get('date')
        
        if not interview_date:
            return Response({"error": "Missing 'date' parameter."}, status=status.HTTP_400_BAD_REQUEST)
        
        slots = ScheduleSlot.objects.filter(interview_date=interview_date, is_booked=False)
        
        if slots.exists():
            
            slot_data = [{"id": slot.id, "start_time": slot.start_time, "is_booked": slot.is_booked, "slot_duration": slot.slot_duration} for slot in slots]
            return Response({"slots": slot_data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No available slots for the selected date."}, status=status.HTTP_404_NOT_FOUND)


class AppointmentViewset(APIView):
        
        def post(self, request):
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid():
                visa_application = serializer.validated_data['visa_application']
                schedule_slot = serializer.validated_data['schedule_slot']
                if Appointment.objects.filter(visa_application=visa_application).exists():
                    return Response(
                        {"message": "An appointment already exists for this visa application."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                if schedule_slot.is_booked:
                    return Response({"message": "This slot is already booked."}, status=status.HTTP_400_BAD_REQUEST)

                schedule_slot.is_booked = True
                schedule_slot.save()
                serializer.save()

                interview_status = request.data.get('interview_status', None)
                if interview_status:
                    serializer.save(interview_status=interview_status)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllInterviewAPI(APIView):

    def get(self, request, pk=None):
        if pk:
            booked_application = get_object_or_404(VisaApplication, appointment__pk=pk)
            serializer = VisaApplicationSerializer(booked_application, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        booked_applications = VisaApplication.objects.filter(appointment__isnull=False).distinct()
        
        interview_date = request.query_params.get('interview_date', None)
        if interview_date:
            booked_applications = booked_applications.filter(appointment__schedule_slot__interview_date=interview_date)

        interview_status = request.query_params.get('interview_status', None)
        if interview_status:
            booked_applications = booked_applications.filter(appointment__interview_status=interview_status)

        serializer = VisaApplicationSerializer(booked_applications, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        interview_date = request.data.get('interview_date')
        start_time = request.data.get('start_time')
        interview_status = request.data.get('interview_status')

        if interview_date:
            appointment.schedule_slot.interview_date = interview_date
        
        if  start_time:
            appointment.schedule_slot.start_time = start_time

        if interview_status:
            appointment.interview_status = interview_status

        appointment.schedule_slot.save()
        appointment.save()

        return Response({"message": "Appointment updated successfully."}, status=status.HTTP_200_OK)

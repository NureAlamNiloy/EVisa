from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Count
from .models import Appointment
from .serializer import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FullyBookedDatesView(APIView):
    permission_classes = [IsAuthenticated]  # Add authentication if required

    def get(self, request):
        # Query to get dates that have 2 or more bookings
        fully_booked_dates = Appointment.objects.values('interview_date') \
                                                .annotate(booking_count=Count('id')) \
                                                .filter(booking_count__gte=2) \
                                                .values_list('interview_date', flat=True)

        # Convert to a list to return as a JSON response
        fully_booked_dates_list = list(fully_booked_dates)
        return Response({'fully_booked_dates': fully_booked_dates_list})



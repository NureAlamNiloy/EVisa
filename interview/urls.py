from django.urls import path
from .views import AppointmentViewset, ScheduleSlotViewset, AdminInterviewInfoViewset



urlpatterns = [
    path('no_interview_dates/', AdminInterviewInfoViewset.as_view(), name="no_interview_dates"),
    path('slot/', ScheduleSlotViewset.as_view(), name="slot"),
    path('appointment/', AppointmentViewset.as_view(), name="appointment"),
]


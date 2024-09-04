from django.urls import path
from .views import AppointmentViewset, ScheduleSlotViewset, NoInterviewViewset



urlpatterns = [
    path('no_interview_dates/', NoInterviewViewset.as_view(), name="no_interview_dates"),
    path('slot/', ScheduleSlotViewset.as_view(), name="slot"),
    path('appointment/', AppointmentViewset.as_view(), name="appointment"),
]


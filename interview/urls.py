from django.urls import path
from .views import AppointmentViewset, ScheduleSlotViewset, AdminInterviewInfoViewset, GetStartEndDate



urlpatterns = [
    path('get_date/', GetStartEndDate.as_view(), name="get_date"),
    path('interview_admin/', AdminInterviewInfoViewset.as_view(), name="no_interview_dates"),
    path('slot/', ScheduleSlotViewset.as_view(), name="slot"),
    path('appointment/', AppointmentViewset.as_view(), name="appointment"),
]


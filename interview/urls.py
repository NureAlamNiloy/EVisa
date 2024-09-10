from django.urls import path
from .views import AllInterviewAPI, AppointmentViewset, ScheduleSlotViewset, AdminInterviewInfoViewset, GetStartEndDate


urlpatterns = [
    path('all_interview/', AllInterviewAPI.as_view(), name="all_interview"),
    path('get_date/', GetStartEndDate.as_view(), name="get_date"),
    path('interview_admin/', AdminInterviewInfoViewset.as_view(), name="no_interview_dates"),
    path('slot/', ScheduleSlotViewset.as_view(), name="slot"),
    path('appointment/', AppointmentViewset.as_view(), name="appointment"),
]


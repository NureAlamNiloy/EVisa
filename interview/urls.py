from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewset, FullyBookedDatesView



router = DefaultRouter()
router.register(r'appointment', AppointmentViewset, basename='appointment')


urlpatterns = [
    path('', include(router.urls)),
    path('booked_dates/', FullyBookedDatesView.as_view(), name="booked_dates"),
]


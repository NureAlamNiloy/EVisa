from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterviewBookingView, InterviewDateView



router = DefaultRouter()
# router.register(r'visaapplication', VisaApplicationViewset, basename='visaapplication')


urlpatterns = [
    path('', include(router.urls)),
    path('date/', InterviewDateView.as_view(), name="date"),
    path('booking/', InterviewBookingView.as_view(), name="booking"),
]



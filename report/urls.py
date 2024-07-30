from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisaStatusReportView, VisaTypeReportView, ApproveRejectReportView



router = DefaultRouter()
# router.register(r'visaapplication', VisaApplicationViewset, basename='visaapplication')


urlpatterns = [
    path('', include(router.urls)),
    path('status-report/', VisaStatusReportView.as_view(), name="status-report"),
    path('type-report/', VisaTypeReportView.as_view(), name="type-report"),
    path('ar-report/', ApproveRejectReportView.as_view(), name="ar-report"),
]



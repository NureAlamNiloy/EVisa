from django.urls import path, include
from .views import VisaStatusReportView, VisaTypeReportView, ApproveRejectReportView




urlpatterns = [
    path('status-report/', VisaStatusReportView.as_view(), name="status-report"),
    path('type-report/', VisaTypeReportView.as_view(), name="type-report"),
    path('ar-report/', ApproveRejectReportView.as_view(), name="ar-report"),
]



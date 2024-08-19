from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisaApplicationViewset, VisaStatusViewset, CountTotalUserApplication



router = DefaultRouter()
router.register(r'visaapplication', VisaApplicationViewset, basename='visaapplication')


urlpatterns = [
    path('', include(router.urls)),
    path('visa-status/<str:tracking_id>/', VisaStatusViewset.as_view(), name="visastatus"),
    path('application-count/<int:user_id>/', CountTotalUserApplication.as_view(), name="visa_count")
]




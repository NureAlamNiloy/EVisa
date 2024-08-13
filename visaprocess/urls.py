from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisaApplicationViewset, VisaStatusViewset



router = DefaultRouter()
router.register(r'visaapplication', VisaApplicationViewset, basename='visaapplication')


urlpatterns = [
    path('', include(router.urls)),
    path('visa-status/<str:tracking_id>/', VisaStatusViewset.as_view(), name="visastatus")
]




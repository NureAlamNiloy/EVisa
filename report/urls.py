from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
# router.register(r'visaapplication', VisaApplicationViewset, basename='visaapplication')


urlpatterns = [
    path('', include(router.urls)),
]



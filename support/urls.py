from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupportViewset


router = DefaultRouter() #eita amader main router
router.register(r'support', SupportViewset, basename='support') # router antena

urlpatterns = [
    path('', include(router.urls)),
]
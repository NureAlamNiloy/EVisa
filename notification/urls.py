from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationView


router = DefaultRouter()
router.register(r'notification', NotificationView, basename='notification')


urlpatterns = [
    path('', include(router.urls)),
    # path('notification/', NotificationView.as_view(), name="notification")
]


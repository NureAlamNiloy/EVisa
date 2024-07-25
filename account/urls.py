from django.urls import path, include
from .views import RegisterView, LoginViewset, LogoutViewset, VerifyOTP
from rest_framework.routers import DefaultRouter


router = DefaultRouter() #eita amader main router


urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegisterView.as_view(), name="register"),
    path('login/', LoginViewset.as_view(), name="login"),
    path('logout/', LogoutViewset.as_view(), name="logout"),
    path('active/', VerifyOTP.as_view(), name="activate"),

]
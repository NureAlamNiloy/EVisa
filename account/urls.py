from django.urls import path, include
from .views import RegisterView,LoginViewset, AdminLoginViewset, VerifyOTP, ChangePasswordView, SendResetPasswordEmailView, ResetPasswordView

urlpatterns = [
    path('register/',RegisterView.as_view(), name="register"),
    path('login/', LoginViewset.as_view(), name="login"),
    path('adminlogin/', AdminLoginViewset.as_view(), name="adminlogin"),
    path('active/', VerifyOTP.as_view(), name="activate"),
    path('changepassword/', ChangePasswordView.as_view(), name="changepassword"),
    path('send-password-reset-email/', SendResetPasswordEmailView.as_view(), name='send-password-reset-email'),
    path('reset-password/<uid>/<token>/', ResetPasswordView.as_view(), name='reset-password'),


]
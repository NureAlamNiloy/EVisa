from .serializer import UserSerializer, LoginSerializer, VerifyAccountSerializer, ChangePasswordSerializer, SendResetPasswordEmailSerializer, ResetPasswordSerializer
from .models import CustomUser
from rest_framework import viewsets, views, permissions, exceptions
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# Generate JWT Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# Create your views here.

class RegisterView(views.APIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            otp = random.randint(1000,9999)
            email_subject = "Confirm Your Email"
            email_body = render_to_string("confirm_email.html", {"otp" : otp})
            email = EmailMultiAlternatives(email_subject, " ", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            user.otp = otp
            user.save()
            return Response({'token': token, "message": "Check your email to verify your account."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(views.APIView):
    serializer_class = VerifyAccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)    
        try:
            if serializer.is_valid():
                email = serializer.validated_data.get("email")
                otp = serializer.validated_data.get("otp")
                user = CustomUser.objects.get(email=email)
                if user.otp != otp:
                    return Response({"message": "Invalid OTP. Check your mail.."}, status=status.HTTP_400_BAD_REQUEST)

                user.is_active = True
                token = get_tokens_for_user(user)
                user.otp = None 
                user.save()
                return Response({
                    'token': token,
                    'user_id': user.id,
                    'username' : user.username,
                    'first_name' : user.first_name ,
                    'last_name' : user.last_name ,
                    'email' : user.email,
                    'phone_no' : user.phone_no,
                    "message": "Registration successful. Your account is now active."
                }, status=status.HTTP_201_CREATED)

        except CustomUser.DoesNotExist:
            return Response({"message": "User not found. Please check your email address."}, status=status.HTTP_400_BAD_REQUEST)




class LoginViewset(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

        if user:
            token = get_tokens_for_user(user)
            login(request, user)
            return Response({
                'token' : token,
                'username' : user.username,
                'first_name' : user.first_name ,
                'last_name' : user.last_name ,
                'email' : user.email,
                'phone_no' : user.phone_no 
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class  LogoutViewset(views.APIView):
    pass

class ChangePasswordView(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ChangePasswordSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get('password')
        password2 = serializer.validated_data.get('password2')
        if password != password2:
            raise ValidationError("Password dosen't match")
        user = request.user
        user.set_password(password)
        user.save()
        return Response({"message":"Password Change Successfully"}, status=status.HTTP_200_OK)


class SendResetPasswordEmailView(views.APIView):
    def post(self, request):
        serializer = SendResetPasswordEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            
            link = f"http://127.0.0.1:8000/account/reset/{uid}/{token}/"
            email_subject = "Reset Your password..."
            email_body = f"This is your reseet password Link {link} Thanks for your co-operation"
            email = EmailMultiAlternatives(email_subject, " ", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({"message":"Password reset Link sent. Please Check Your Email"}, status=status.HTTP_200_OK)
        else:
            raise exceptions.ValidationError("This Email dosen't Exists")
        
class ResetPasswordView(views.APIView):
    def post(self, request, uid, token):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get('password')
        password2 = serializer.validated_data.get('password2')
        if password != password2:
            raise exceptions.ValidationError("Password dosen't match")
            
        id = smart_str(urlsafe_base64_decode(uid))
        user = CustomUser.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise exceptions.ValidationError("Token dosen't match")

        user.set_password(password)
        user.save()
        return Response({"message":"Password Reset Successfully"}, status=status.HTTP_200_OK)



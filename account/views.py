from .serializer import UserSerializer, LoginSerializer, VerifyAccountSerializer
from .models import CustomUser
from rest_framework import viewsets, views, permissions, exceptions
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string





# Create your views here.

class RegisterView(views.APIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = random.randint(1000,9999)
            email_subject = "Confirm Your Email"
            email_body = render_to_string("confirm_email.html", {"otp" : otp})
            email = EmailMultiAlternatives(email_subject, " ", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            user.otp = otp
            user.save()
            return Response({"message": "Check your email to verify your account."}, status=status.HTTP_201_CREATED)
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
                token, created = Token.objects.get_or_create(user=user)
                user.otp = None 
                user.save()
                return Response({
                    'token': token.key,
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
    authentication_classes = [SessionAuthentication]
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username' : user.username,
                'first_name' : user.first_name ,
                'last_name' : user.last_name ,
                'email' : user.email,
                'phone_no' : user.phone_no 
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutViewset(views.APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            tokens_deleted, _ = Token.objects.filter(user=request.user).delete()
            if tokens_deleted > 0:
                logout(request)
                return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Token not found or already deleted"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "You are not logged in."}, status=status.HTTP_400_BAD_REQUEST)


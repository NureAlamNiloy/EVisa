from .serializer import UserSerializer, LoginSerializer
from .models import CustomUser
from rest_framework import viewsets, views, permissions, exceptions
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string





# Create your views here.



class RegisterView(views.APIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uniqueId = urlsafe_base64_encode(force_bytes(user.pk))
            email_link = f"http://127.0.0.1:8000/account/active/{uniqueId}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string("confirm_email.html", {"email_link" : email_link})

            email = EmailMultiAlternatives(email_subject, " ", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for verify")
        return Response(serializer.errors)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = CustomUser._default_manager.get(pk=uid)
    except(CustomUser.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
         
 

class LoginViewset(views.APIView):
    
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
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutViewset(views.APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            tokens_deleted, _ = Token.objects.filter(user=request.user).delete()
            if tokens_deleted > 0:
                logout(request)
                return redirect('login')
            else:
                return Response({"error": "Token not found or already deleted"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
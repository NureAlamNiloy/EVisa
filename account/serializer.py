from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_no = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email','phone_no','password','password2']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        phone_no = self.validated_data['phone_no']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':"Password Dosen't Match"})
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"This Email already exists"})
        
        account = CustomUser(username=username, email=email, phone_no=phone_no, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

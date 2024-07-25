from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    first_name = models.CharField(verbose_name="First_name", max_length=200)
    last_name = models.CharField(verbose_name="Last_name", max_length=200)
    email = models.EmailField( max_length=254, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    phone_no = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_no']




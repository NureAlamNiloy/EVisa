from django.db import models
from account.models import CustomUser

# Create your models here.

class UserSupport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    massage_date = models.DateTimeField(auto_now=True)





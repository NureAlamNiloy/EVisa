from django.db import models
from account.models import CustomUser
# from visaprocess.models import VisaApplication, VisaStatus
# from interview.models import InterviewBooking

# Create your models here.

class notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    



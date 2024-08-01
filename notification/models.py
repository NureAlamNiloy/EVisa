from django.db import models
from account.models import CustomUser
from visaprocess.models import VisaApplication, VisaStatus
from interview.models import InterviewBooking

# Create your models here.

class notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    visa_application = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    visa_status = models.ForeignKey(VisaStatus, on_delete=models.CASCADE)
    interview_booking = models.ForeignKey(InterviewBooking, on_delete=models.CASCADE)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    


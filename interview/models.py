from django.db import models
from account.models import CustomUser
from visaprocess.models import VisaApplication, VisaStatus
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

class InterviewDate(models.Model):
    interview_date = models.DateField(unique=True)
    max_interview = models.IntegerField(default=3)

    def is_available(self):
        return self.booking_slot.count() <= self.max_interview

class InterviewBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slot = models.ForeignKey(InterviewDate, related_name="booking_slot", on_delete=models.CASCADE)
    visa_application = models.OneToOneField(VisaApplication, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"user: {self.visa_application.user.username}  applicant: {self.visa_application.full_name}"
    
    
    def save(self, *args, **kwargs):
        if not self.slot.is_available():
            raise ValidationError("This date is already fully booked.")
        super().save(*args, **kwargs)
        self.booking_Confermation_mail()
    
    def booking_Confermation_mail(self):
        subject = f"Your interview date & Time"
        body = f"Dear {self.visa_application.full_name} Your inter slot is confirm. Your Interview Date is {self.slot.interview_date}. Please Make sure you are in time in the consulate"
        mail = [self.visa_application.email]
        send_mail(subject,body, settings.EMAIL_HOST_USER, mail)
    




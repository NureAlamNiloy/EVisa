from django.db import models
from visaprocess.models import VisaApplication
from account.models import CustomUser

# Create your models here.

class NoInterview(models.Model):
    no_interview_date = models.DateField()

    def __str__(self):
        return f"No Interview at {self.no_interview_date}"

class ScheduleSlot(models.Model):
    interview_date = models.DateField()
    start_time = models.TimeField(default="9:00")   
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.interview_date}===={self.is_booked}" 



class Appointment(models.Model):
    visa_application = models.ForeignKey(VisaApplication,related_name='appointment', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    schedule_slot = models.OneToOneField(ScheduleSlot, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['visa_application', 'schedule_slot'] 
    
    def __str__(self):
        return self.visa_application.full_name
    
    



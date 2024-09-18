from django.db import models
from visaprocess.models import VisaApplication
from account.models import CustomUser

# Create your models here.

class AdminInterviewInfo(models.Model):
    total_interview = models.IntegerField(default=20)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(default="09:00")
    end_time = models.TimeField(default="18:00")

    def __str__(self):
        return f"No Interview at {self.no_interview_date}"

class ScheduleSlot(models.Model):
    interview_date = models.DateField() 
    start_time = models.TimeField(default="09:00")
    is_booked = models.BooleanField(default=False)
 
    def __str__(self):
        return f"{self.interview_date}={self.start_time}" 



class Appointment(models.Model):
    visa_application = models.ForeignKey(VisaApplication, related_name="appointment", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    schedule_slot = models.OneToOneField(ScheduleSlot, related_name="appointment", on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['visa_application', 'schedule_slot'] 
    
    def __str__(self):
        return self.visa_application.full_name
    

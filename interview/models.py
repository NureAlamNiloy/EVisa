from django.db import models
from visaprocess.models import VisaApplication
from account.models import CustomUser

# Create your models here.

class Appointment(models.Model):
    visa_application = models.ForeignKey(VisaApplication,related_name='appointment', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interview_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['visa_application', 'interview_date'] 
    
    def __str__(self):
        return self.visa_application.full_name
    
    



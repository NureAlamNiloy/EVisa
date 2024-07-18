from django.db import models
from account.models import CustomUser
from visaprocess.models import VisaApplication

# Create your models here.

class notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    visa_application = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    massage = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    


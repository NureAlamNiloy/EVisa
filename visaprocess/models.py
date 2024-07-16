from django.db import models
from account.models import CustomUser

# Create your models here.
VISA_TYPE = [
    ('Tourist', 'Tourist'),
    ('Business', 'Business'),
    ('Student', 'Student'),
    ('Work', 'Work'),
    ('Medical', 'Medical'),
    ('Femily', 'Femily')
]
GENDER = [
    ('Mail', 'Mail'),
    ('Femail', 'Femail'),
    ('Others', 'Others'),
]

class VisaApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    visa_type = models.CharField(max_length=20, choices=VISA_TYPE)
    gender = models.CharField(max_length=30, choices=GENDER )
    
    passport_no = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    
    submission_date = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username









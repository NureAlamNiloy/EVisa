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

class VisaApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    visa_type = models.CharField(max_length=20, choices=VISA_TYPE)
    application_date = models.DateTimeField(auto_now_add=True)
    passport_no = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    







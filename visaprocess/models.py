from django.db import models
from account.models import CustomUser
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

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
    full_name = models.CharField(max_length=255)
    visa_type = models.CharField(max_length=20, choices=VISA_TYPE)
    gender = models.CharField(max_length=30, choices=GENDER )
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=30)
    passport_no = models.CharField(max_length=20)
    passport_issue_date = models.DateField()
    passport_expiry_date = models.DateField()
    country_of_passport_issuance = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=20)
    occupation = models.CharField(max_length=40)
    present_address = models.TextField()
    permanent_address  = models.TextField()
    city = models.CharField(max_length=40)
    state_province = models.CharField(max_length=50)
    postal_code = models.IntegerField
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    purpose_of_visit  = models.TextField()
    planned_duration_of_stay = models.IntegerField()
    accommodation_details  = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_relationship = models.CharField(max_length=20)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_email = models.EmailField()
    health_information = models.FileField(upload_to='health/')
    educational_background = models.CharField(max_length=255)
    applicant_signature = models.FileField(upload_to='signeture/')
    passport_photo = models.FileField(upload_to='passport/')
    user_photo = models.FileField(upload_to='applicantPhoto/')
    health_ensurence = models.FileField(upload_to='health/')
    is_approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    is_modified = models.BooleanField(default=False)
    submission_date = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}, applicant: {self.full_name}"

VISASTATUS = [
    ('Panding', 'Panding'),
    ('AdminApprove', 'AdminApprove'),
    ('PoliceVerification', 'PoliceVerification'),
    ('Approved', 'Approved'),
]
class VisaStatus(models.Model):
    visa_application = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    traking_id = models.CharField(max_length=250, null=True, blank=True)
    visa_status = models.CharField(max_length=100, default='Panding', choices=VISASTATUS)
    massage = models.TextField()
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_status = VisaStatus.objects.get(pk=self.pk).visa_status
            if old_status != self.visa_status:
                subject = f"Your visa application is now on {self.visa_status}"
                massage = f"{self.massage}"
                mail = [self.visa_application.email]
                send_mail(subject, massage, settings.EMAIL_HOST_USER, mail)
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['update_at']






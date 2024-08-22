
from django.db import models
from account.models import CustomUser
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import os
import uuid

# Create your models here.
VISA_TYPE = [
    ('Tourist', 'Tourist'),
    ('Business', 'Business'),
    ('Student', 'Student'),
    ('Work', 'Work'),
    ('Medical', 'Medical'),
    ('Family', 'Family')
]
GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
]


def travel_insurance_upload_to(instance, filename):
    return f"thumbnail_images/{instance.full_name}_{instance.user.id}{os.path.splitext(filename)[1]}"

def applicant_signature_upload_to(instance, filename):
    return f"signeture/{instance.full_name}_{instance.user.id}{os.path.splitext(filename)[1]}"

def passport_photo_upload_to(instance, filename):
    return f"passport/{instance.full_name}_{instance.user.id}{os.path.splitext(filename)[1]}"

def user_photo_upload_to(instance, filename):
    return f"applicant_photo/{instance.full_name}_{instance.user.id}{os.path.splitext(filename)[1]}"

def health_ensurence_upload_to(instance, filename):
    return f"health_ensurence/{instance.full_name}_{instance.user.id}{os.path.splitext(filename)[1]}"


class VisaApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
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
    purpose_of_visit  = models.TextField()
    planned_duration_of_stay = models.IntegerField()
    accommodation_details  = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_relationship = models.CharField(max_length=20)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_email = models.EmailField()
    educational_background = models.CharField(max_length=255)
    user_photo = models.ImageField(upload_to=user_photo_upload_to)
    travel_insurance = models.ImageField(upload_to=travel_insurance_upload_to)
    applicant_signature = models.ImageField(upload_to=applicant_signature_upload_to)
    passport_photo = models.ImageField(upload_to=passport_photo_upload_to)
    health_ensurence = models.ImageField(upload_to=health_ensurence_upload_to)
    is_approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    is_modified = models.BooleanField(default=False)
    submission_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}, applicant: {self.full_name}"
 
VISASTATUS = [
    ('Pending', 'Pending'),
    ('AdminApprove', 'AdminApprove'),
    ('PoliceVerification', 'PoliceVerification'),
    ('Approved', 'Approved'),
]
class VisaStatus(models.Model):
    visa_application = models.ForeignKey(VisaApplication, on_delete=models.CASCADE, related_name='visa_statuses')
    tracking_id = models.CharField(max_length=250, unique=True, null=True, blank=True)
    visa_status = models.CharField(max_length=100, default='Pending', choices=VISASTATUS)
    message = models.TextField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_status = VisaStatus.objects.get(pk=self.pk).visa_status
            if old_status != self.visa_status:
                subject = f"Visa application Update {self.visa_status}"
                message = render_to_string("status.html", {'visa_status': self.visa_status, 'message': self.message, 'tracking_id': self.tracking_id})
                email = EmailMultiAlternatives(subject, " ", to=[self.visa_application.email])
                email.attach_alternative(message, "text/html")
                email.send()
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['update_at']
        verbose_name_plural = "Visa Status"
    
    def __str__(self):
        return f"Applicant: {self.visa_application.full_name}"




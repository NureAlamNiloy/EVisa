from django.db import models
from account.models import CustomUser
from visaprocess.models import VisaApplication
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class UserPayment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    visaApplication = models.OneToOneField(VisaApplication, on_delete=models.CASCADE)
    is_payment = models.BooleanField(default=False)
    checkOut_id = models.CharField(max_length=800)

@receiver(post_save, sender=CustomUser)
def create_user_payment(instance, created, **kwargs):
    if created:
        UserPayment.objects.create(user=instance)


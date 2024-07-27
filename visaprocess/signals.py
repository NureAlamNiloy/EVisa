from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VisaApplication, VisaStatus
import random
import string


@receiver(post_save, sender=VisaApplication)
def create_VisaStatus(sender, instance, created, **kwargs):
    if created:
        VisaStatus.objects.create(visa=instance, traking_id=create_TrakingId)

def create_TrakingId():
    return ''.join(random.choices(string.ascii_letters+string.digits, k=10))





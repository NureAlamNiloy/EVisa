from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VisaApplication, VisaStatus
import random
import string


@receiver(post_save, sender=VisaApplication)
def create_VisaStatus(sender, instance, created, **kwargs):
    if created:
        tracking_id = create_TrakingId()
        VisaStatus.objects.create(visa_application=instance, traking_id=tracking_id)
def create_TrakingId():
    while True:
        tracking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
        if not VisaStatus.objects.filter(traking_id=tracking_id).exists():
            return tracking_id

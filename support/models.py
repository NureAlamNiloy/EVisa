from django.db import models

# Create your models here.

class UserSupport(models.Model):
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    massage_date = models.DateTimeField(auto_now=True)





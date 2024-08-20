from django.contrib import admin
from .models import VisaApplication, VisaStatus

# Register your models here.

class VisaApplicationAdmin(admin.ModelAdmin):
    list_display = ["id","user", "full_name", "is_approved","rejected"]

class VisaStatusAdmin(admin.ModelAdmin):
    list_display = ["id","visa_application", "visa_status", "tracking_id"]

admin.site.register(VisaApplication, VisaApplicationAdmin)
admin.site.register(VisaStatus, VisaStatusAdmin)


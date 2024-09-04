from django.contrib import admin
from .models import notification

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

admin.site.register(notification, NotificationAdmin)


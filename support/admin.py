from django.contrib import admin
from .models import UserSupport

# Register your models here.

class SupportAdmin(admin.ModelAdmin):
    list_display = ['user','subject', 'massage_date']


admin.site.register(UserSupport, SupportAdmin)

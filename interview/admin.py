from django.contrib import admin
from .models import Appointment,ScheduleSlot, NoInterview

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id", "visa_application","user","schedule_slot"]
class ScheduleSlotAdmin(admin.ModelAdmin):
    list_display = ["id", "interview_date","is_booked"]
class NoInterviewAdmin(admin.ModelAdmin):
    list_display = ["id", "no_interview_date"]

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(ScheduleSlot, ScheduleSlotAdmin)
admin.site.register(NoInterview, NoInterviewAdmin)

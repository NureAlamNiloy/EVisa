from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin 

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "email","first_name","last_name", "is_active"]
    list_filter = ["is_active"]
    fieldsets = [
        (None, {"fields": ["username","email", "password"]}),
        ("Personal info", {"fields": ["first_name","last_name", "otp"]}),
        ("Permissions", {"fields": ["is_active","is_superuser", "is_staff"]}),
    ]

    search_fields = ["email","username"]
    ordering = ["email","id"]
    filter_horizontal = []

admin.site.register(CustomUser, CustomUserAdmin)

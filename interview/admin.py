from django.contrib import admin
from .models import InterviewDate, InterviewBooking



from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import InterviewBooking

class InterviewBookingForm(ModelForm):
    class Meta:
        model = InterviewBooking
        fields = '__all__'

class InterviewBookingAdmin(admin.ModelAdmin):
    form = InterviewBookingForm

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            form.add_error(None, e)
            self.message_user(request, e.message, level='error')


admin.site.register(InterviewDate)
admin.site.register(InterviewBooking, InterviewBookingAdmin)



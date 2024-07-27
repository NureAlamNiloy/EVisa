from django.apps import AppConfig


class VisaprocessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visaprocess'
    def ready(self):
        import visaprocess.signals

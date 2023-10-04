from django.apps import AppConfig


class HospitalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hospitals"
    
    # register signals
    # ready() Method: The ready() method is called when the Django application is fully loaded
    # and ready to use. It's a good approach to register signals when the app is ready.
    def ready(self):
        import hospitals.signals
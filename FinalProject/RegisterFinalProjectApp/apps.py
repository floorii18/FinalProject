from django.apps import AppConfig


class RegisterfinalprojectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RegisterFinalProjectApp'
    
    def ready(self):
        import RegisterFinalProjectApp.signals

from django.apps import AppConfig


class BasefinalprojectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BaseFinalProjectApp'

    def ready(self):
        import BaseFinalProjectApp.signals
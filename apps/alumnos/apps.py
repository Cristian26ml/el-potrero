from django.apps import AppConfig


class AlumnosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.alumnos'

    def ready(self):
        import apps.alumnos.signals

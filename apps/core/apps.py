from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self):
        from apps.core.custom_admin import admin_site
        from django.contrib import admin

        from apps.alumnos.models import Alumno
        from apps.calendario.models import Evento
        from apps.logros.models import Trofeo
        from apps.galeria.models import Media
        from apps.usuarios.models import Profile
        from apps.core.models import Programa, Auspiciador
        from apps.programas.models import Programa
        from apps.contacto.models import MensajeContacto

        class AlumnoAdmin(admin.ModelAdmin):
            list_display = ("nombre", "apellido", "apoderado",
                            "fecha_nacimiento", "email", "telefono", "fecha_inscripcion")

        class EventoAdmin(admin.ModelAdmin):
            list_display = ("titulo", "fecha", "tipo_evento")

        class TrofeoAdmin(admin.ModelAdmin):
            list_display = ("nombre", "descripcion", "año")

        class MediaAdmin(admin.ModelAdmin):
            list_display = ("tipo", "url_original", "archivo", "fecha_subida")

        class ProgramaAdmin(admin.ModelAdmin):
            list_display = ("nombre_programa", "horario",
                            "ubicacion", "fecha_creacion")
            search_fields = ("nombre_programa", "ubicacion")
            list_filter = ("ubicacion",)

        class AuspiciadorAdmin(admin.ModelAdmin):
            list_display = ("nombre", "descripcion")

        admin_site.register(Alumno, AlumnoAdmin)
        admin_site.register(Evento, EventoAdmin)
        admin_site.register(Trofeo, TrofeoAdmin)
        admin_site.register(Media, MediaAdmin)
        admin_site.register(Programa, ProgramaAdmin)
        admin_site.register(Auspiciador, AuspiciadorAdmin)

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

        def exportar_csv(modeladmin, request, queryset):
            import csv
            from django.http import HttpResponse
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = "attachment; filename=alumnos.csv"
            writer = csv.writer(response)
            writer.writerow(["Nombre", "Apellido", "Email"])
            for alumno in queryset:
                writer.writerow([alumno.nombre, alumno.apellido, alumno.email])
            return response

        exportar_csv.short_description = "Exportar seleccionados a CSV"

        class AlumnoAdmin(admin.ModelAdmin):
            list_display = ("nombre", "apellido", "apoderado",
                            "fecha_nacimiento", "email", "telefono", "fecha_inscripcion")
            actions = [exportar_csv]

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

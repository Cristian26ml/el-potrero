import json
from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from apps.contacto.models import MensajeContacto


class CustomAdminSite(admin.AdminSite):
    site_header = "El Potrero - Administración"
    site_title = "El Potrero"
    index_title = "Panel de Control"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("", self.admin_view(self.dashboard), name="index"),
        ]
        return custom_urls + urls

    def dashboard(self, request):
        from apps.alumnos.models import Alumno
        from apps.calendario.models import Evento
        from apps.logros.models import Trofeo
        from apps.galeria.models import Media
        from apps.usuarios.models import Profile
        from apps.programas.models import Programa

        inscripciones_por_mes = (
            Alumno.objects
            .annotate(mes=TruncMonth("fecha_inscripcion"))
            .values("mes")
            .annotate(total=Count("id"))
            .order_by("mes")
        )

        usuarios_por_rol = {
            "Administradores": Profile.objects.filter(rol="admin").count(),
            "Entrenadores": Profile.objects.filter(rol="entrenador").count(),
            "Apoderados": Profile.objects.filter(rol="apoderado").count(),
            "Alumnos": Profile.objects.filter(rol="alumno").count(),
        }

        programas_count = Programa.objects.filter(activo=True).count()

        context = dict(
            self.each_context(request),
            alumnos_count=Alumno.objects.count(),
            eventos=Evento.objects.order_by("fecha")[:5],
            trofeos_count=Trofeo.objects.count(),
            roles=json.dumps(list(usuarios_por_rol.keys())),
            cantidades=json.dumps(list(usuarios_por_rol.values())),
            fotos_count=Media.objects.filter(tipo="foto").count(),
            videos_count=Media.objects.filter(tipo="video").count(),
            meses=json.dumps([i["mes"].strftime("%b %Y")
                             for i in inscripciones_por_mes]),
            totales=json.dumps([i["total"] for i in inscripciones_por_mes]),
            programas_count=programas_count,
        )
        return TemplateResponse(request, "admin/index.html", context)


admin_site = CustomAdminSite(name="custom_admin")


class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "mensaje", "fecha_envio")
    search_fields = ("nombre", "correo")
    list_filter = ("fecha_envio",)


admin_site.register(MensajeContacto, MensajeContactoAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

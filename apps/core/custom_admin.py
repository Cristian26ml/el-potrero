from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from apps.contacto.models import MensajeContacto

# 1. Definimos primero el sitio administrador personalizado


class CustomAdminSite(admin.AdminSite):
    site_header = "El Potrero - Administración"
    site_title = "El Potrero"
    index_title = "Panel de Control"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Esto reemplaza el index por defecto con tu dashboard personalizado
            path("", self.admin_view(self.dashboard), name="index"),
        ]
        return custom_urls + urls

    def dashboard(self, request):
        from apps.alumnos.models import Alumno
        from apps.calendario.models import Evento
        from apps.logros.models import Trofeo
        from apps.galeria.models import Media
        from apps.usuarios.models import Profile

        usuarios_por_rol = {
            "Administradores": Profile.objects.filter(rol="admin").count(),
            "Entrenadores": Profile.objects.filter(rol="entrenador").count(),
            "Apoderados": Profile.objects.filter(rol="apoderado").count(),
            "Alumnos": Profile.objects.filter(rol="alumno").count(),
        }

        context = dict(
            self.each_context(request),
            alumnos_count=Alumno.objects.count(),
            eventos=Evento.objects.order_by("fecha")[:5],
            trofeos_count=Trofeo.objects.count(),
            roles=list(usuarios_por_rol.keys()),
            cantidades=list(usuarios_por_rol.values()),
            fotos_count=Media.objects.filter(tipo="foto").count(),
            videos_count=Media.objects.filter(tipo="video").count(),
        )
        return TemplateResponse(request, "admin/index.html", context)


# 2. Instanciamos el sitio personalizado
admin_site = CustomAdminSite(name="custom_admin")


# 3. Definimos el ModelAdmin
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "mensaje", "fecha_envio")
    search_fields = ("nombre", "correo")
    list_filter = ("fecha_envio",)


# 4. Registramos el modelo en la instancia que YA EXISTE arriba
admin_site.register(MensajeContacto, MensajeContactoAdmin)

from django.contrib import admin
from apps.alumnos.models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono",
                    "pago_confirmado", "estado_inscripcion")
    list_filter = ("pago_confirmado", "estado_inscripcion")
    search_fields = ("nombre", "apellido", "email", "telefono")
    fields = ("nombre", "apellido", "fecha_nacimiento", "apoderado",
              "email", "telefono", "pago_confirmado", "estado_inscripcion")
    readonly_fields = ("fecha_inscripcion",)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.estado_inscripcion == "activo" and obj.user:
            user = obj.user
            user.first_name = obj.nombre
            user.last_name = obj.apellido
            user.email = obj.email
            user.save()
            print(f"✅ User {user.username} actualizado con datos de Alumno")

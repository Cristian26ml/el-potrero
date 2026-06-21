# Usamos CustomAdminSite en apps/core/admin.py
# apps/alumnos/admin.py
from django.contrib import admin
from .models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email",
                    "pago_confirmado", "user", "password_temporal")
    # no editable, solo visible
    readonly_fields = ("user", "password_temporal")
    list_filter = ("pago_confirmado",)

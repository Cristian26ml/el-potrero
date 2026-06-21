# Usamos CustomAdminSite en apps/core/admin.py
from django.contrib import admin
from .models import Programa


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre_programa", "horario", "ubicacion", "activo")
    list_filter = ("activo",)

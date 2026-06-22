from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "rol", "telefono", "estado_inscripcion")
    search_fields = ("user__username", "rol", "telefono")
    list_filter = ("rol", "estado_inscripcion")
    fields = ("user", "rol", "telefono", "estado_inscripcion")


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name",
                    "last_name", "is_staff", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "is_superuser")

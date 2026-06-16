# apps/usuarios/models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('entrenador', 'Entrenador'),
        ('apoderado', 'Apoderado'),
        ('alumno', 'Alumno'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES, default='alumno')
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.rol})"

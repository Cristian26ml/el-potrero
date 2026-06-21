# apps/alumnos/models.py
from django.db import models
from django.contrib.auth.models import User


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    apoderado = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    pago_confirmado = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    # Campo solo para pruebas
    password_temporal = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

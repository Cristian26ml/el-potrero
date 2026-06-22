# apps/alumnos/models.py
from django.db import models
from django.contrib.auth.models import User


class Alumno(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("activo", "Activo"),
        ("rechazado", "Rechazado"),
    ]

    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    apoderado = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    pago_confirmado = models.BooleanField(default=False)
    estado_inscripcion = models.CharField(
        max_length=20, choices=ESTADOS, default="pendiente")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.estado_inscripcion}"

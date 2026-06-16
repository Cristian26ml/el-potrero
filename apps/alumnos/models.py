# apps/alumnos/models.py
from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    apoderado = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

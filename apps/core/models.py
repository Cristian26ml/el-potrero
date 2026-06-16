# apps/core/models.py
from django.db import models


class Programa(models.Model):
    nombre_programa = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)

    alumnos = models.ManyToManyField(
        'alumnos.Alumno', related_name='programas')

    def __str__(self) -> str:
        return str(self.nombre_programa)


class Auspiciador(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='auspiciadores/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.nombre)

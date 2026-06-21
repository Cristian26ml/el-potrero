from django.db import models


class Programa(models.Model):
    nombre_programa = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_programa

# apps/logros/models.py
from django.db import models


class Trofeo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    año = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.año})"


class Partido(models.Model):
    fecha = models.DateField()
    rival = models.CharField(max_length=100)
    resultado = models.CharField(max_length=50)

    def __str__(self):
        return f"Vs {self.rival} - {self.fecha}"


class Entrenamiento(models.Model):
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(
        help_text="Duración en minutos", blank=True, null=True)

    def __str__(self):
        return f"Entrenamiento {self.categoria} - {self.fecha}"


class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    lugar = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.año})"

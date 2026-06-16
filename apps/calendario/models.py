# apps/calendario/models.py
from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField()
    tipo_evento = models.CharField(max_length=50, choices=[
        ('entrenamiento', 'Entrenamiento'),
        ('partido', 'Partido'),
        ('reunion', 'Reunión'),
    ])

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"

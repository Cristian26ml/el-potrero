# apps/calendario/models.py
from django.db import models

TIPOS_EVENTO = [
    ("partido", "Partido"),
    ("entrenamiento", "Entrenamiento"),
    ("reunion", "Reunión"),
    ("torneo", "Torneo"),
]


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField()
    tipo_evento = models.CharField(max_length=50, choices=[
        ('entrenamiento', 'Entrenamiento'),
        ('partido', 'Partido'),
        ('reunion', 'Reunión'),
        ('torneo', 'Torneo')
    ])

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"

# apps/alumnos/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.alumnos.models import Alumno


@receiver(post_save, sender=Alumno)
def sincronizar_user(sender, instance, **kwargs):
    """
    Cada vez que se guarda un Alumno, si está activo y vinculado a un User,
    sincroniza nombre, apellido y correo al modelo User.
    """
    if instance.estado_inscripcion == "activo" and instance.user:
        user = instance.user
        user.first_name = instance.nombre
        user.last_name = instance.apellido
        user.email = instance.email
        user.save()

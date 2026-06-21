# apps/alumnos/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.alumnos.models import Alumno


@receiver(post_save, sender=Alumno)
def crear_usuario_para_alumno(sender, instance, created, **kwargs):
    if created and instance.pago_confirmado:
        # Generar contraseña temporal
        temp_password = User.objects.make_random_password()

        # Crear usuario asociado
        user = User.objects.create_user(
            username=f"{instance.nombre.lower()}.{instance.apellido.lower()}",
            email=instance.email,
            password=temp_password,
            first_name=instance.nombre,
            last_name=instance.apellido,
        )

        # Guardar referencia en Alumno
        instance.user = user
        instance.password_temporal = temp_password
        instance.save()

        # Aquí podrías enviar el password temporal por correo o WhatsApp
        print(f"Usuario creado: {user.username} / Contraseña: {temp_password}")

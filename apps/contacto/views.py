from django.shortcuts import render, redirect
from .models import MensajeContacto


def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        MensajeContacto.objects.create(
            nombre=nombre,
            correo=correo,
            mensaje=mensaje
        )
        return redirect("contacto")  # recarga la página después de enviar

    return render(request, "contacto/contacto.html")

from django.shortcuts import render, redirect
from .models import MensajeContacto
from django.contrib import messages


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
        messages.success(request, "Tu mensaje fue enviado con éxito ✅")
        return redirect("contacto")

    return render(request, "contacto/contacto.html")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from apps.core.models import Programa
from apps.alumnos.models import Alumno


class CustomLoginView(LoginView):
    template_name = "usuarios/login.html"


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registro exitoso ⚽. Ahora puedes iniciar sesión.")
            return redirect("login")  # redirige al login
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registro.html", {"form": form})


def inscripcion(request):
    programas = Programa.objects.all()
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        apoderado = request.POST.get("apoderado")
        telefono = request.POST.get("telefono")
        programa_id = request.POST.get("programa")

        programa = Programa.objects.get(id=programa_id)
        Alumno.objects.create(
            nombre=nombre,
            edad=edad,
            apoderado=apoderado,
            telefono=telefono,
            programa=programa
        )
        return redirect("home")  # o a una página de confirmación

    return render(request, "usuarios/inscripcion.html", {"programas": programas})

from django.shortcuts import render, redirect
from .forms import AlumnoForm


def inscripcion(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "alumnos/inscripcion_exitosa.html")
        else:
            return render(request, "alumnos/inscripcion.html", {"form": form})
    else:
        form = AlumnoForm()
    return render(request, "alumnos/inscripcion.html", {"form": form})

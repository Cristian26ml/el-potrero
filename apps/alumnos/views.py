from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlumnoForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='aviso_inscripcion')
def inscripcion(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.user = request.user
            alumno.estado_inscripcion = "pendiente"
            alumno.save()
            messages.success(
                request, "Inscripción enviada. Espera validación del administrador.")
            return redirect("home")
        else:
            return render(request, "alumnos/inscripcion.html", {"form": form})
    else:
        form = AlumnoForm()
    return render(request, "alumnos/inscripcion.html", {"form": form})

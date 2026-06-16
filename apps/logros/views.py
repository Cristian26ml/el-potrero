from django.shortcuts import render
from .models import Partido, Entrenamiento, Torneo, Trofeo


def logros(request):
    context = {
        "partidos_count": Partido.objects.count(),
        "entrenamientos_count": Entrenamiento.objects.count(),
        "torneos_count": Torneo.objects.count(),
        "trofeos": Trofeo.objects.all(),
    }
    return render(request, "logros/logros.html", context)

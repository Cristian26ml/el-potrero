from django.shortcuts import render
from apps.logros.models import Partido, Entrenamiento, Torneo
from apps.programas.models import Programa
from apps.calendario.models import Evento
from apps.galeria.models import Media


def home(request):
    partidos_count = Evento.objects.filter(tipo_evento="partido").count()
    entrenamientos_count = Evento.objects.filter(
        tipo_evento="entrenamiento").count()
    torneos_count = Evento.objects.filter(tipo_evento="torneo").count()

    galeria_preview = Media.objects.filter(
        tipo="foto").order_by("-fecha_subida")[:4]

    context = {
        "galeria": galeria_preview,
        "partidos_count": partidos_count,
        "entrenamientos_count": entrenamientos_count,
        "torneos_count": torneos_count,
    }
    return render(request, "core/home.html", context)


def programas(request):
    programas = Programa.objects.all()
    return render(request, "programas/programas.html", {"programas": programas})


def calendario(request):
    eventos = Evento.objects.all().order_by("fecha")
    return render(request, "calendario/calendario.html", {"eventos": eventos})


def galeria(request):
    return render(request, "core/galeria.html")


def logros(request):
    context = {
        "partidos_count": Evento.objects.filter(tipo_evento="partido").count(),
        "entrenamientos_count": Evento.objects.filter(tipo_evento="entrenamiento").count(),
        "torneos_count": Evento.objects.filter(tipo_evento="torneo").count(),
    }
    return render(request, "logros/logros.html", context)


def contacto(request):
    return render(request, "contacto/contacto.html")


def sobre_nosotros(request):
    return render(request, "core/sobre_nosotros.html")

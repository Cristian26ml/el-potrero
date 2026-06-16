from django.shortcuts import render
from apps.galeria.models import Media


def galeria(request):
    galeria_preview = Media.objects.filter(
        tipo="foto").order_by("-fecha_subida")
    return render(request, "galeria/galeria.html", {"galeria": galeria_preview})

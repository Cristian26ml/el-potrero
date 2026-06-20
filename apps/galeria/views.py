from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.galeria.models import Media


@login_required
def galeria(request):
    galeria_preview = Media.objects.filter(
        tipo="foto").order_by("-fecha_subida")
    return render(request, "galeria/galeria.html", {"galeria": galeria_preview})

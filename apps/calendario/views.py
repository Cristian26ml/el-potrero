from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Evento


@login_required
def calendario(request):
    eventos = Evento.objects.all().order_by('fecha')
    return render(request, "calendario/calendario.html", {"eventos": eventos})

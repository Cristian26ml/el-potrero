# apps/programas/views.py
from django.shortcuts import render
from .models import Programa


def programas(request):
    programas = Programa.objects.all()
    return render(request, "programas/programas.html", {"programas": programas})

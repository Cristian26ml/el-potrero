# apps/programas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("programas/", views.programas, name="programas"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('inscripcion/', views.inscripcion, name='inscripcion'),
]

from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'apoderado',
                  'email', 'telefono']
        exclude = ['user', 'pago_confirmado',
                   'estado_inscripcion', 'fecha_inscripcion']

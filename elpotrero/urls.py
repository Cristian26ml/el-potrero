"""
URL configuration for elpotrero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from apps.core.custom_admin import admin_site
from apps.usuarios import views

# Desactiva el autodiscover del admin estándar
from django.contrib import admin
admin.autodiscover = lambda: None  # ← evita que cargue admin.py prematuramente

urlpatterns = [
    path("admin/", admin_site.urls),
    path("", include("apps.core.urls")),
    path("registro/", views.registro, name="registro"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("usuarios/", include("apps.usuarios.urls")),
    path("", include("apps.alumnos.urls")),
    path("", include("apps.calendario.urls")),
    path("", include("apps.logros.urls")),
    path("", include("apps.contacto.urls")),
]

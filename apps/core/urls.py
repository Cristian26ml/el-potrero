from django.urls import path
from apps.core import views as core_views
from apps.galeria import views as galeria_views
from apps.contacto import views as contacto_views

urlpatterns = [
    path("", core_views.home, name="home"),
    path("programas/", core_views.programas, name="programas"),
    path("calendario/", core_views.calendario, name="calendario"),
    path("galeria/", galeria_views.galeria, name="galeria"),
    path("logros/", core_views.logros, name="logros"),
    path("contacto/", contacto_views.contacto, name="contacto"),
    path("sobre-nosotros/", core_views.sobre_nosotros, name="sobre_nosotros"),

]

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("inscripcion/", views.inscripcion, name="inscripcion"),
]

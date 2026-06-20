from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("logout/", LogoutView.as_view(next_page="/",
         http_method_names=["get", "post"]), name="logout"),
    path("inscripcion/", views.inscripcion, name="inscripcion"),
    path("password_change/", PasswordChangeView.as_view(
        template_name="usuarios/password_change.html"
    ), name="password_change"),
    path("password_change/done/", PasswordChangeDoneView.as_view(
        template_name="usuarios/password_change_done.html"
    ), name="password_change_done"),
]

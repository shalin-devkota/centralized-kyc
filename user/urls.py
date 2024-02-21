from django.urls import path

from .views import is_loggedin


urlpatterns = [
    path("check/", is_loggedin, name="login-view"),
]

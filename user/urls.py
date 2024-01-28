from django.urls import path
from .views import RegisterUser, GetUserData

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="user-register"),
    path("data/", GetUserData.as_view(), name="user-data"),
]

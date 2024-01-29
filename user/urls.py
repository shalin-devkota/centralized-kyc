from django.urls import path
from .views import RegisterUser, GetUserData, CreateUser

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("register/", RegisterUser.as_view(), name="user-register"),
    path("data/", GetUserData.as_view(), name="user-data"),
    path("create/", CreateUser.as_view(), name="user-create"),
    path("login/", TokenObtainPairView.as_view(), name="login-view"),
]

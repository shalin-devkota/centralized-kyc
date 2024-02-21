from django.urls import path
from .views import check_bank

urlpatterns = [
    path(
        "check/",
        check_bank,
        name="check-bank",
    )
]

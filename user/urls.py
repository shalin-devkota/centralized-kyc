from django.urls import path
from .views import get_email_view,verify_email

urlpatterns=[
    path("init/",get_email_view,name="test-view"),
    path("verify-email/",verify_email,name="verify-email")
]
from django.contrib import admin
from .models import VerifiedUser, AuthUser

# Register your models here.
admin.site.register(VerifiedUser)
admin.site.register(AuthUser)

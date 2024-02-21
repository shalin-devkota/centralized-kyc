from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from uuid import uuid4
import os


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("role", "regulator")

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, password, **other_fields)


def upload_cit_front(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"citizenship_front.{ext}"

    return os.path.join("citizenships", str(instance.citizenship_number), new_filename)


def upload_cit_back(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"citizenship_back.{ext}"

    return os.path.join("citizenships", str(instance.citizenship_number), new_filename)


def upload_photo(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{instance.citizenship_number}.{ext}"

    return os.path.join("photos", str(instance.citizenship_number), new_filename)


# Create your models here.
class VerifiedUser(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    first_name = models.CharField(max_length=50, null=False, blank=False)
    middle = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    nid_number = models.CharField(max_length=20, null=True, blank=True, unique=True)

    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=False, blank=False
    )

    birth_date_bs = models.DateField(
        null=False, blank=False, auto_now=False, auto_created=False
    )

    nationality = models.CharField(max_length=30, null=False, blank=False)

    citizenship_number = models.CharField(
        max_length=20, unique=True, null=False, blank=False
    )
    citizen_issued_district = models.CharField(max_length=50, null=False, blank=False)
    citizen_issued_date_bs = models.DateField(
        null=False, blank=False, auto_created=False, auto_now=False
    )
    photo = models.ImageField(upload_to=upload_photo)
    citizenship_front = models.ImageField(upload_to=upload_cit_front)
    citizenship_back = models.ImageField(upload_to=upload_cit_back)

    permanent_address_district = models.CharField(
        max_length=50, null=False, blank=False
    )
    permanent_address_municipality = models.CharField(
        max_length=50, null=False, blank=False
    )
    permanent_address_ward = models.CharField(max_length=50, null=False, blank=False)
    permanent_address_tol = models.CharField(max_length=100, blank=False, null=False)

    current_address_district = models.CharField(max_length=50, null=False, blank=False)
    current_address_municipality = models.CharField(
        max_length=50, null=False, blank=False
    )
    current_address_ward = models.CharField(max_length=50, null=False, blank=False)
    current_address_tol = models.CharField(max_length=100, blank=False, null=False)
    signature = models.UUIDField(default=uuid4, unique=True, editable=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}"


class AuthUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("regulator", "Regulator"),
        ("bank", "Bank"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, null=False, blank=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["role"]

    def __str__(self):
        return self.email

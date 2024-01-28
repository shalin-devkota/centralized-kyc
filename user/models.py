from django.db import models
from uuid import uuid4
import os


def file_upload_param(file_type):
    def file_upload(instance, filename):
        print("Yes", instance.citizenship_number)
        ext = filename.split(".")[-1]
        new_filename = f"{instance.citizenship_number}_{file_type}.{ext}"
        if file_type == "photo":
            return os.path.join(
                "photos", str(instance.citizenship_number), new_filename
            )
        else:
            return os.path.join(
                "citizenships", str(instance.citizenship_number), new_filename
            )

    return file_upload


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
    photo = models.ImageField(upload_to=file_upload_param(file_type="photo"))
    citizenship_front = models.ImageField(
        upload_to=file_upload_param(file_type="citizenship_front")
    )
    citizenship_back = models.ImageField(
        upload_to=file_upload_param(file_type="citizenship_back")
    )

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

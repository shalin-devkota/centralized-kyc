from django.db import models

# Create your models here.
class VerifiedUser(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=50,null=False,blank=False)
    middle = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=False,blank=False)

    nid_number  = models.CharField(max_length=20,null=True,blank=True)

    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,null=False,blank=False)

    birth_date_bs = models.DateField(null=False,blank=False,auto_now=False,auto_created=False)

    nationality = models.CharField(max_length=30,null=False,blank=False)

    citizenship_number = models.CharField(max_length=20,unique=True,null=False,blank=False)
    citizen_issued_district = models.CharField(max_length=50,null=False,blank=False)
    citizen_issued_date_bs = models.DateField(null=False,blank=False,auto_created=False,auto_now=False)

    permanent_address_district = models.CharField(max_length=50,null=False,blank=False)
    permanent_address_municipality = models.CharField(max_length=50,null=False,blank=False)
    permanent_address_ward = models.CharField(max_length=50,null=False,blank=False)
    permanent_address_tol = models.CharField(max_length=100,blank=False,null=False)

    current_address_district = models.CharField(max_length=50,null=False,blank=False)
    current_address_municipality = models.CharField(max_length=50,null=False,blank=False)
    current_address_ward = models.CharField(max_length=50,null=False,blank=False)
    current_address_tol = models.CharField(max_length=100,blank=False,null=False)

   
    def __str__(self):
        return f"{self.first_name}"
    

   
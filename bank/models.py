from django.db import models
import uuid
# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100,unique=True,null=False,blank=False)
    head_office = models.CharField(max_length=100,null=False,blank=False)
    access_key = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)

    def __str__(self):
        return f"{self.name}"
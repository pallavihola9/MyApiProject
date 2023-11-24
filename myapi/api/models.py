import uuid
from django.db import models

# Create your models here.



class RegisterUser(models.Model):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.CharField(max_length=14,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    

    def __str__(self):
        return f"{self.name} - {self.unique_identity}"

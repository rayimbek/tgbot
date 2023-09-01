from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
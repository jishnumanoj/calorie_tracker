from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True)

    weight = models.CharField(max_length=15)

    height = models.CharField(max_length=15)

    age = models.PositiveIntegerField()

    dob = models.DateField(null=True)
    
from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.TextField(max_length=200, unique=True)

class House(models.Model):
    address = models.TextField(max_length=200, unique=True)
    owner = models.ForeignKey(Owner)
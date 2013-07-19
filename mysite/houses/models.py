from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.TextField(max_length=200)

class House(models.Model):
    address = models.TextField(max_length=200)
    owner = models.ForeignKey(Owner)
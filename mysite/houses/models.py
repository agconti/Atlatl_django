from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.TextField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

class House(models.Model):
    address = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    owner = models.ManyToManyField(Owner)
from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = (models.CharField(max_length=5))
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
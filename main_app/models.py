from django.db import models
from django.urls import reverse


# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = (models.CharField(max_length=5))
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def _str_(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

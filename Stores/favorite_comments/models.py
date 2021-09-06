from django.db import models
from django.conf import settings

from products.models import Products

# Create your models here.

class Comments(models.Model):
    id_products=models.ForeignKey(Products, on_delete=models.CASCADE)
    id_person=models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    comments=models.CharField(max_length=100)

    def __str__(self):
        return self.comments

class Favorite(models.Model):
    id_products=models.ForeignKey(Products, on_delete=models.CASCADE)
    id_person=models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_person)  
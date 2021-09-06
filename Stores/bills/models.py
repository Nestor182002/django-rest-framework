from django.db import models

from django.conf import settings
from products.models import Products


# Create your models here.
class Bills(models.Model):
    client_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    bill_product=models.ManyToManyField(Products)
    state=models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
    
    

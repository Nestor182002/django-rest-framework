from django.db import models
#ignals
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=70)
    description=models.TextField()
    price=models.IntegerField(null=False,default=0)

    def __str__(self):
        return self.name

class NewRegisterProducts(models.Model):
    products=models.ForeignKey(Products, on_delete=models.CASCADE)
    create_add = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Products) 
def create_register(sender, instance, created, **kwargs):
    if created:
        NewRegisterProducts.objects.create(products=instance)
   

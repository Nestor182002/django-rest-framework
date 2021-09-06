from django.contrib import admin
from django.contrib.auth.models import Permission
from products.models import Products,NewRegisterProducts

# Register your models here.
admin.site.register(Products)
admin.site.register(NewRegisterProducts)
admin.site.register(Permission)

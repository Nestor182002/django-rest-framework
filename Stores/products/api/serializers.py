from django.db.models import fields
from rest_framework import serializers
# products
from products.models import Products

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Products
        fields=('id','name','description','price')

    
        
        
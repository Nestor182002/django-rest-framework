from rest_framework import serializers
# products
from favorite_comments.models import Favorite , Comments



class ProductsSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model=Favorite
        fields=('id','id_products')



    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id_favorite':instance.id,
            'products':[{
                 'id':instance.id_products.id,
                 'name':instance.id_products.name,
                 'description':instance.id_products.description,
                 'price':instance.id_products.price
                 }],
            
        }

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Comments
        fields=('id','id_products','comments')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id_comment':instance.id,
            'products':[{
                 'id':instance.id_products.id,
                 }],
            'comments':[{
                 'data':instance.comments,
                 }],
            
        }
    
        
        
from rest_framework import viewsets

# products
from products.models import Products
# serializer
from products.api.serializers import ProductsSerializer
# permisos
from rest_framework.permissions import IsAdminUser, AllowAny

class ProductsView(viewsets.ModelViewSet):
    """
    Products
    """
    serializer_class = ProductsSerializer
    

    def get_queryset(self):
        return Products.objects.all()

    def get_permissions(self):

        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'update':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'create':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            self.permission_classes = [AllowAny]
       
        return super(ProductsView,self).get_permissions()
    
    


   
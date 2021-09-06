from django.test import TestCase
from products.models import Products


class TestProducts(TestCase):
    def setUp(self):
        Products.objects.create(name='Big', description='texto de prueba',price=123)
        
    def test_products_nameequals(self):
        Product=Products.objects.get(id=1)
        name=Product.name
        self.assertEquals(name,"Big")
        
        
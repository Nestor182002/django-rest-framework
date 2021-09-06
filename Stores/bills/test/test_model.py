from django.test import TestCase
from favorite_comments.models import Comments
from django.contrib.auth import get_user_model
from products.models import Products

User=get_user_model()
class TestComments(TestCase):
    def setUp(self):
        user=User.objects.create(username="pepe",password="prueba1",email="nestor@hotmail.com")
        product=Products.objects.create(name='Big', description='texto de prueba',price=1234)
        Comments.objects.create(id_products=product,id_person=user,comments="prueba")
        
    def test_comments_name(self):
        comment=Comments.objects.get(id=1)
        comentario=comment.comments
        
        self.assertEquals(comentario,"prueba")

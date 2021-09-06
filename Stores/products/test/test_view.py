from django.test import TestCase


class TestProducts(TestCase):
    
            
    def test_views_list(self):
        resp = self.client.get('/products/')
        self.assertEqual(resp.status_code, 200)
    
    def test_views_access_denied_normal_user(self):
        resp = self.client.post('/products/',data={'name':'nestor','description':'texto de prueba','price':123})
        self.assertEqual(resp.status_code,403)
from django.test import TestCase
from .models import ProductCategories,Product,ProductImage
# Create your tests here.


class TestProductsViews(TestCase):
    def test_root_is_valid_url(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        
    def test_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/home.html")
        
    def test_get_create_item(self):
        resp = self.client.get("/product_add/")
        self.assertEqual(resp.status_code, 200)
        
   
        
    
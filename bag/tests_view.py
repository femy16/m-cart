from django.test import TestCase
from products.models import Product
from products.views import product_details

# Create your tests here.
class TestBagViews(TestCase):
    
    def test_view_bag(self):
        page = self.client.get("/bag/view_bag")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bag/view_bag.html")
        
    def test_get_404_on_add_to_bag_with_no_game_id(self):
        response = self.client.get("/bag/add/")
        self.assertEqual(response.status_code, 404)
    
        
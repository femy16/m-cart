from django.apps import apps
from django.test import TestCase
from .apps import PlaceOrderConfig

class TestPlaceOrderConfig(TestCase):

    def test_products_app(self):
        self.assertEqual("place_order", PlaceOrderConfig.name)
        self.assertEqual("place_order", apps.get_app_config("place_order").name)
    
    def test_placeorder_redirects_to_Login_if_not_Loggedin(self):
        response = self.client.get("/placeorder/")
        self.assertRedirects(response, '/accounts/login/?next=/placeorder/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
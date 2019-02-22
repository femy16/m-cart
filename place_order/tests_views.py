from django.test import TestCase
from .forms import MakePaymentForm
class TestPlaceOrderviews(TestCase):

    
    
    def test_placeorder_redirects_to_Login_if_not_Loggedin(self):
        response = self.client.get("/placeorder/")
        self.assertRedirects(response, '/accounts/login/?next=/placeorder/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_payment(self):
        form_params={
             'credit_card_number': '3333222211110000',
            'cvv': '100',
            'expiry_month': '5',
            'expiry_year': '2022',
            'stripe_id': '********HiddenInput***********'
        }
        response = self.client.post("/", form_params)
        form = MakePaymentForm(form_params)
        self.assertTrue(form.is_valid())
        
    
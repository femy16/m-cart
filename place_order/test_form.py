from django.test import TestCase
from .forms import MakePaymentForm

class TestPlaceOrderForms(TestCase):
    
     def test_Payment_form(self):
        form=MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '5',
            'expiry_year': '2022',
            'stripe_id': '*******************'
        })
        self.assertTrue(form.is_valid())
        
     
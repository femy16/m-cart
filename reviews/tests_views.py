from django.apps import apps
from django.test import TestCase
from .apps import ReviewsConfig
from .forms import ReviewForm

class TestReviewsadding(TestCase):

    
        
    def test_review_add(self):
        form_params={
            'title': 'Nice',
            'content': 'Wonderful Product',
        }
        response = self.client.post("/product_details/reviews/", form_params)
        form = ReviewForm(form_params)
        self.assertTrue(form.is_valid())  
        
    def test_error_1_review_add(self):
        form_params={
            'title': '',
            'content': 'Wonderful Product',
        }
        response = self.client.post("/product_details/reviews/", form_params)
        form = ReviewForm(form_params)
        self.assertFalse(form.is_valid())  
        
    def test_error_2_review_add(self):
        form_params={
            'title': 'Nice',
            'content': '',
        }
        response = self.client.post("/product_details/reviews/", form_params)
        form = ReviewForm(form_params)
        self.assertFalse(form.is_valid()) 
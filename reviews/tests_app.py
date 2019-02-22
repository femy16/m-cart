from django.apps import apps
from django.test import TestCase
from .apps import ReviewsConfig
from .forms import ReviewForm

class TestReviewsConfig(TestCase):

    def test_reviews_app(self):
        self.assertEqual("reviews", ReviewsConfig.name)
        self.assertEqual("reviews", apps.get_app_config("reviews").name)
        
    def test_error_on_registration(self):
        form_params={
            'title': 'Nice',
            'content': 'Wonderful Product',
        }
        response = self.client.post("/product_details/reviews/", form_params)
        form = ReviewForm(form_params)
        self.assertTrue(form.is_valid())  
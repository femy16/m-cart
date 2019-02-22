from django.test import TestCase
from .forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your tests here.
class TestAccountsForms(TestCase):
    
   
        
    def test_registration_form(self):
        form=UserCreationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertTrue(form.is_valid())
    
    
        
            
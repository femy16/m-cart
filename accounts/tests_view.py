# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserCreationForm

# Create your tests here.
class TestAccountsViews(TestCase):
    
    
     def test_get_signup_page(self):
        page = self.client.get("/accounts/signup/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/signup.html")
        
     def test_get_Login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/login.html")
        
     def test_user_can_register(self):
        response = self.client.post("/accounts/signup/", {
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'Fortest123',
            'password2': 'Fortest123'
        })
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
     def test_user_can_log_in(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="Fortest123")
        response = self.client.post("/accounts/login", {
            'username': 'test',
            'password': 'Fortest123'
        })
        response = self.client.get('/accounts/login')
        
     def test_user_does_not_exist(self):
        form_params = self.client.post("/accounts/login", {
            'username': 'test',
            'password': 'pass0word'
        })
        response = self.client.post("/accounts/login", form_params)
        form = UserCreationForm(form_params)
        self.assertFalse(form.is_valid())  
        
     def test_error_on_registration(self):
        form_params={
            'username': 'test2',
            'email': 'test@email.com',
            'password1': 'Fortes123',
            'password2': 'Fortest123'
        }
        response = self.client.post("/accounts/signup", form_params)
        form = UserCreationForm(form_params)
        self.assertFalse(form.is_valid())  